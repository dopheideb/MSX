import logging
import queue
import re
import sys
from   typing import Self
import z80
import z80.disasm.instruction

class Disasm:
    def __init__(self: Self, filename: str=None) -> None:
        self.seen = {}
        self.disasm = {}
        self.z80 = z80.Z80()
        self.z80.PC = 0x4000
        
        if filename is not None:
            rom = open(filename, 'rb').read()
            self.z80.set_ram(bytes=rom, offset=0x4000)
        self.z80.load_instruction_set('z80.disasm.instruction')
    
    def add_routine(self: Self, address: int, routine_name: str) -> None:
        z80.disasm.instruction.aux.add_routine(address, routine_name)
    def get_routine(self: Self, address: int) -> str:
        return z80.disasm.instruction.aux.get_routine(address)
    
    def run(self: Self) -> dict:
        pc_queue = queue.Queue()
        pc_queue.put(self.z80.ram.get_word(0x4002))
        
        def hkeyi_hook(offset, new_value, old_value):
            vdp_hook = self.z80.ram.get_word(0xFD9B)
            logging.debug(f'vdp_hook=0x{vdp_hook:04X}')
            pc_queue.put(vdp_hook)
        self.z80._ram.register_write_callback(hkeyi_hook, 0xFD9C)
        while not pc_queue.empty():
            pc = pc_queue.get()
            if pc in self.seen:
                logging.debug(f'[{pc:04X}] Ignoring already seen PC.')
                continue
            if pc < 0x4000:
                continue
            self.seen[pc] = 'code'
            self.z80.PC = pc
            try:
                self.z80.fetch_opcode()
                instr = self.z80.execute_opcode()
            except NotImplementedError:
            #except ValueError:
            #except KeyError as e:
                logging.exception(f'Bailing out because of unknown opcode at pc {pc:04X}: 0x{e.args[0]:02X}')
                break
            self.disasm[pc] = str(instr)
            instr_name = type(instr).__name__
            
            match instr.name():
                case 'CALL nn' | 'CALL cc, nn':
                    logging.debug(f"Adding CALL destination 0x{instr.nn:04X} also to queue.")
                    pc_queue.put(self.z80.PC)
                    pc_queue.put(instr.nn)
                case "LD (nn), HL":
                    if instr.nn == 0xFDA9:
                        pass
                case 'JP nn':
                    logging.debug(f"{pc:04X}: 'JP nn' encountered. Only branching to 0x{instr.nn:04X}.")
                    pc_queue.put(instr.nn)
                case "JR e":
                    jump_destination = self.z80.PC + instr.e
                    logging.debug(f"{pc:04X}: '{instr.name()}' encountered. Only branching to 0x{jump_destination:04X}.")
                    pc_queue.put(jump_destination)
                case "JR C, e" |\
                     "JR NC, e" |\
                     "JR Z, e" |\
                     "JR NZ, e":
                    jump_destination = self.z80.PC + instr.e
                    logging.debug(f"{pc:04X}: '{instr.name()}' encountered. Also branching to 0x{jump_destination:04X}.")
                    pc_queue.put(self.z80.PC)
                    pc_queue.put(jump_destination)
                case 'RET':
                    logging.debug(f"{pc:04X}: 'RET' encountered. Discontinuing this branch.")
                case _:
                    logging.debug(f"[{pc:04X}] Enqueueing PC={self.z80.PC:04X}. Handled {instr_name}.")
                    pc_queue.put(self.z80.PC)
            
            logging.debug(f'DISASM: {type(instr).__name__} ' + str(instr))
        
        return self.disasm
