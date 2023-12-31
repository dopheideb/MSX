import collections
import logging
import queue
import re
import sys
from   typing import Self, Optional
import z80
import z80.disasm.instruction
import z80.z80dasm.instruction

class Disasm:
    def __init__(self: Self, filename: Optional[str]=None) -> None:
        self.disasm = collections.defaultdict(lambda: collections.defaultdict(dict))
        self.z80 = z80.Z80()
        self.z80.PC = 0x4000
        
        if filename is not None:
            rom = open(filename, 'rb').read()
            for offset, value in enumerate(rom):
                self.z80.ram[0x4000 + offset] = value
            
            self.HL_plus_is_A = rom.find(b'\x85\x6F\xD0\x24\xC9')
            if self.HL_plus_is_A == -1:
                self.HL_plus_is_A = None
            else:
                self.HL_plus_is_A += 0x4000
                self.add_routine(self.HL_plus_is_A, 'HL += A')
                
                self.PC_magic = rom.find(b'\x87\xe1\xcd' + self.HL_plus_is_A.to_bytes(2, 'little') + b'\x5e\x23\x56\xeb\xe9')
                if self.PC_magic == -1:
                    self.PC_magic = None
                else:
                    self.PC_magic += 0x4000
                    self.add_routine(self.PC_magic, 'PC = PC[2 * A]')
        self.z80.load_instruction_set('z80.disasm.instruction', overwrite=True)
        #self.z80.load_instruction_set('z80.z80dasm.instruction', overwrite=True)
    
    def add_routine(self: Self, address: int, routine_name: str) -> None:
        z80.disasm.instruction.aux.add_routine(address, routine_name)
    def get_routine(self: Self, address: int) -> str:
        return z80.disasm.instruction.aux.get_routine(address)
    
    def run(self: Self, style: Optional[str]=None):
        match style:
            case None | 'branch all':
                return self.run_branch_all()
            case 'linear':
                return self.run_linear()
            case _:
                raise ValueError(f"Unknown run style '{style}'")
    
    def run_branch_all(self: Self) -> dict:
        pc_queue = queue.Queue()
        pc_queue.put(self.z80.ram.get_word(0x4002))
        
        def hkeyi_hook(offset, new_value, old_value):
            vdp_hook = self.z80.ram.get_word(0xFD9B)
            logging.debug(f'vdp_hook=0x{vdp_hook:04X}')
            pc_queue.put(vdp_hook)
            self.disasm[vdp_hook]['type'] = 'code'
            self.disasm[vdp_hook]['from'][0xFD9B] = 'VDP hook'
        self.z80._ram.register_write_callback(hkeyi_hook, 0xFD9C)
        
        while not pc_queue.empty():
            pc = pc_queue.get()
            if pc in self.disasm and 'disasm' in self.disasm[pc]:
                logging.debug(f'[{pc:04X}] Ignoring already disassembled/handled PC.')
                continue
            if pc < 0x4000:
                ## Don't disassemble BIOS routines.
                continue
            self.disasm[pc]['type'] = 'code'
            self.z80.PC = pc
            
            try:
                self.z80.fetch_opcode()
                instr = self.z80.execute_opcode()
            except NotImplementedError as e:
                logging.exception(f'Bailing out because of unknown opcode at pc {pc:04X}: 0x{e.args[0]:02X}')
                break
            self.disasm[pc]['disasm'] = str(instr)
            instr_name = type(instr).__name__
            
            match instr.name():
                case "CALL nn" | "CALL cc, nn":
                    pc_queue.put(self.z80.PC)
                    self.disasm[self.z80.PC]['from'][instr._PC] = instr.name()
                    
                    logging.debug(f"Adding CALL destination {instr.nn} also to queue.")
                    pc_queue.put(instr._nn)
                    self.disasm[instr._nn]['from'][instr._PC] = instr.name()
                    
                    if self.PC_magic is not None and instr._nn == self.PC_magic:
                        offset = instr._PC + 3
                        last_jump = None
                        while True:
                            jump = self.z80._ram.get_word(offset)
                            if last_jump is None:
                                last_jump = jump
                            if abs(jump - last_jump) >= 0x400:
                                break
                            offset += 2
                            logging.debug(f'[{offset:04X}] Part of a jump table. Jump to 0x{jump:04X}.')
                            pc_queue.put(jump)
                case "JP nn":
                    logging.debug(f"{pc:04X}: 'JP nn' encountered. Only branching to {instr.nn}.")
                    pc_queue.put(instr._nn)
                    self.disasm[instr._nn]['from'][instr._PC] = instr.name()
                case "JR e":
                    logging.debug(f"{pc:04X}: '{instr.name()}' encountered. Only branching to {instr.jump_destination}.")
                    pc_queue.put(instr._jump_destination)
                    self.disasm[instr._jump_destination]['from'][instr._PC] = instr.name()
                case "DJNZ, e"  |\
                     "JR C, e"  |\
                     "JR NC, e" |\
                     "JR Z, e"  |\
                     "JR NZ, e":
                    pc_queue.put(self.z80.PC)
                    
                    logging.debug(f"{pc:04X}: '{instr.name()}' encountered. Also branching to {instr.jump_destination}.")
                    
                    pc_queue.put(instr._jump_destination)
                    self.disasm[instr._jump_destination]['from'][instr._PC] = instr.name()
                case "RET":
                    logging.debug(f"{pc:04X}: 'RET' encountered. Discontinuing this branch.")
                case _:
                    logging.debug(f"[{pc:04X}] Enqueueing PC={self.z80.PC:04X}. Handled {instr_name}.")
                    self.disasm[self.z80.PC]['from'][instr._PC] = 'fall through'
                    pc_queue.put(self.z80.PC)
            
            logging.debug(f'DISASM: {type(instr).__name__} ' + str(instr))
        
        return self.disasm

    def run_linear(self: Self) -> dict:
        self.z80.PC = 0x4000
        
        while self.z80.PC < 0x8000:
            try:
                self.z80.fetch_opcode()
                instr = self.z80.execute_opcode()
            except NotImplementedError as e:
                logging.exception(f'Bailing out because of unknown opcode at pc {pc:04X}: 0x{e.args[0]:02X}')
                break
            self.disasm[self.z80.PC]['disasm'] = str(instr)
            instr_name = type(instr).__name__

        return self.disasm
