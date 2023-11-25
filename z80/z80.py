import logging
from   typing import Self
import z80.instruction
import z80.ram
#import z80.registers



class Z80:
    def __init__(self: Self):
        self._ram = z80.ram.RAM(size=128 * 1024)
        self._opcode2handler = {}
        self.registers = z80.registers.Registers()
        
        for instruction_string in z80.instruction.instruction_set:
            instruction_object = getattr(z80.instruction, instruction_string)(
                self.registers,
                self._ram
            )
            for opcode in instruction_object.opcodes():
                self._opcode2handler[opcode] = instruction_object
    
    def stepi(self: Self):
        self.fetch_opcode()
        self.handle_opcode()
    
    def fetch_opcode(self: Self) -> None:
        #logging.debug(f'Fetching opcode at PC=0x{self.PC:04X}.')
        self._opcode = self._ram[self.registers.PC]
        if self._opcode != 0xCB and self._opcode != 0xED:
            logging.debug(f'Fetched opcode at PC=0x{self.PC:04X}: 0x{self._opcode:02X}')
        else:
            self._opcode <<= 8
            self._opcode |= self._ram[self.registers.PC + 1]
            logging.debug(f'Fetched opcode at PC=0x{self.PC:04X}: 0x{self._opcode:04X}')
    
    def handle_opcode(self: Self) -> None:
        try:
            handler = self._opcode2handler[self._opcode]
            PC = self.registers.PC
            handler.handle(self._opcode)
            
            ## Instructions like RET change the program counter. Keep 
            ## those changes.
            if PC == self.registers.PC:
                self.registers.PC += handler.size()
        except KeyError:
            logging.debug(f'Unknown opcode 0x{self._opcode:02X}.')
            raise
    
    
    
    @property
    def A(self: Self) -> int:
        return self.registers.A.val
    
    @A.setter
    def A(self: Self, value: int) -> int:
        self.registers.A.val = value
    
    
    
    @property
    def PC(self: Self) -> int:
        return self.registers.PC
    
    @PC.setter
    def PC(self: Self, value: int) -> int:
        self.registers.PC = value
    
    
    
    @property
    def ram(self: Self):
        return self._ram
    
    #@ram.setter
    def set_ram(self: Self, bytes: bytes, offset: int=0):
        self._ram[offset:len(bytes)] = bytes
