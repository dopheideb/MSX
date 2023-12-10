import logging
from   typing import Self, Type
import z80.instruction
import z80.instructions
import z80.ram



class Z80:
    def __init__(self: Self):
        self._ram = z80.ram.RAM(size=128 * 1024)
        self._opcode2instruction = {}
        self.registers = z80.registers.Registers()
        
        self.load_instruction_set('z80.instructions')
    
    def load_instruction_set(self: Self, instruction_set: str, overwrite=False) -> None:
        logging.debug(f"Loading instruction set with name '{instruction_set}'.")
        for instruction in z80.instruction.Instruction.instruction_sets[instruction_set]:
            logging.debug(f"Loading instruction {instruction}.")
            self.add_instruction(instruction, overwrite)
    
    def add_instruction(self: Self, instruction_class: Type[z80.instruction.Instruction], overwrite: bool=False) -> None:
        for opcode in instruction_class.opcodes():
            if not overwrite and opcode in self._opcode2instruction:
                error = f'Tried to overwrite opcode 0x{opcode:02X} with overwrite=False. Opcode is already tied to {str(self._opcode2instruction[opcode])}.'
                logging.error(error)
                raise ValueError(error)
            self._opcode2instruction[opcode] = instruction_class
    
    def override_instruction(self: Self, instruction_class: Type[z80.instruction.Instruction]) -> None:
        self.add_instruction(instruction_class, overwrite=True)
    
    def stepi(self: Self):
        self.fetch_opcode()
        self.execute_opcode()
    
    def fetch_opcode(self: Self) -> None:
        #logging.debug(f'Fetching opcode at PC=0x{self.PC:04X}.')
        self._opcode = self._ram[self.registers.PC]
        if self._opcode not in [0xCB, 0xDD, 0xED, 0xFD]:
            logging.debug(f'Fetched opcode at PC=0x{self.PC:04X}: 0x{self._opcode:02X}')
        else:
            ## 0xCB  : Bit instructions
            ## 0xDD  : IX instructions
            ## 0xDDCB: IX bit instructions
            ## 0xED  : Miscellaneous instructions
            ## 0xFD  : IY instructions
            ## 0xFDCB: IY bit instructions
            self._opcode <<= 8
            self._opcode |= self._ram[self.registers.PC + 1]
            if self._opcode not in [0xDDCB, 0xFDCB]:
                logging.debug(f'Fetched opcode at PC=0x{self.PC:04X}: 0x{self._opcode:04X}')
            else:
                ## 0xDDCB: IX bit instrunctions. The order is weird. For 
                ## example, the RES 6, (IX+3) is: 0xDDCB03B6. Note that 
                ## operand 'd' (0x03) is in between opcode 0xDDCB and 
                ## opcode 0xB6.
                ##
                ## 0xFDCB: IY bit instructions. Same weirdness.
                self._opcode <<= 8
                self._opcode |= self._ram[self.registers.PC + 3]
                logging.debug(f'Fetched opcode at PC=0x{self.PC:04X}: 0x{self._opcode:06X}')
    
    def decode_instruction(self: Self) -> z80.instruction.Instruction:
        try:
            instruction = self._opcode2instruction[self._opcode](
                ram=self._ram,
                registers=self.registers,
                opcode=self._opcode,
            )
        except KeyError:
            logging.exception(f'Unknown opcode 0x{self._opcode:02X}.')
            raise
        return instruction
    
    def execute_opcode(self: Self) -> z80.instruction.Instruction:
        instruction = self.decode_instruction()
        logging.debug('\t\t\t\t\t' + str(instruction))
        self.registers.PC += instruction.size
        if hasattr(instruction, 'execute'):
            instruction.execute()
        return instruction
    
    
    
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
    def set_ram(self: Self, bytes: bytes, offset: int) -> None:
        self._ram[offset:len(bytes)] = bytes
