import logging
from   typing import Self, Type
import z80.instruction
import z80.ram
#import z80.registers



class Z80:
    def __init__(self: Self):
        self._ram = z80.ram.RAM(size=128 * 1024)
        self._opcode2instruction = {}
        self.registers = z80.registers.Registers()
        
        for instruction_string in z80.instruction.instruction_set:
            instruction_object = getattr(z80.instruction, instruction_string)(
                self.registers,
                self._ram
            )
            for opcode in instruction_object.opcodes:
                self._opcode2instruction[opcode] = instruction_object
    
    def override_instruction(self: Self, instruction_class: Type[z80.instruction.Instruction]):
    #def override_instruction(self: Self, instruction_class):
        instruction_object = instruction_class(
            self.registers,
            self._ram
        )
        logging.debug('HIER!!!')
        logging.debug(instruction_object)
        logging.debug(instruction_object.opcodes)
        for opcode in instruction_object.opcodes:
            self._opcode2instruction[opcode] = instruction_object

    
    def stepi(self: Self):
        self.fetch_opcode()
        self.execute_opcode()
    
    def fetch_opcode(self: Self) -> None:
        #logging.debug(f'Fetching opcode at PC=0x{self.PC:04X}.')
        self._opcode = self._ram[self.registers.PC]
        if self._opcode != 0xCB and self._opcode != 0xED:
            logging.debug(f'Fetched opcode at PC=0x{self.PC:04X}: 0x{self._opcode:02X}')
        else:
            self._opcode <<= 8
            self._opcode |= self._ram[self.registers.PC + 1]
            logging.debug(f'Fetched opcode at PC=0x{self.PC:04X}: 0x{self._opcode:04X}')
    
    def execute_opcode(self: Self) -> None:
        try:
            instruction = self._opcode2instruction[self._opcode]
            instruction.load(self._opcode)
            logging.debug('\t\t\t\t\t' + str(instruction))
            self.registers.PC += instruction.size
            if hasattr(instruction, 'execute'):
                instruction.execute()
        except KeyError:
            logging.debug(f'Unknown opcode 0x{self._opcode:02X}.')
            raise
    
    
    
    ## Convenience
    @property
    def A(self: Self) -> int:
        return self.registers.A
    @A.setter
    def A(self: Self, value: int) -> None:
        self.registers.A = value
    
    
    
    @property
    def PC(self: Self) -> int:
        return self.registers.PC
    
    @PC.setter
    def PC(self: Self, value: int) -> None:
        self.registers.PC = value
    
    
    
    @property
    def ram(self: Self) -> z80.ram.RAM:
        return self._ram
    
    #@ram.setter
    def set_ram(self: Self, bytes: bytes, offset: int=0) -> None:
        self._ram[offset:len(bytes)] = bytes
