import abc
import logging
import sys
from   typing import Self, List
import z80.ram
import z80.registers



instruction_set =\
[
    'CALL_nn',
    'DI',
    'IM_1',
    'LD_dd_nn',
    'LD_deref_HL_n',
    'LD_deref_nn_A',
    'LD_deref_nn_HL',
    'LD_r_n',
    'LD_r_n',
    'LDIR',
    'RET',
    'XOR_n',
    'XOR_r',
]

class Instruction(abc.ABC):
    def __init__(self: Self,
        registers: z80.registers.Registers,
        ram: z80.ram.RAM,
    ) -> None:
        self._registers = registers
        self._ram = ram
        self._opcode = 0x00	## NOP
    
    def load(self: Self, opcode: int) -> None:
        self._opcode = opcode
    
    @property
    def opcode(self: Self) -> int: return self._opcode
    
    @property
    @abc.abstractmethod
    def opcodes(self: Self) -> List[int]: pass
    
    @property
    @abc.abstractmethod
    def size(self: Self) -> int: pass

    #@abc.abstractmethod
    #def handle(self: Self, opcode: int) -> None: pass



_r2n =\
{
    0b111: 'A',
    0b000: 'B',
    0b001: 'C',
    0b010: 'D',
    0b011: 'E',
    0b100: 'H',
    0b101: 'L',
}

_dd2n =\
{
    0b00: 'BC',
    0b01: 'DE',
    0b10: 'HL',
    0b11: 'SP',
}

class CALL_nn(Instruction):
    @property
    def opcodes(self: Self) -> List[int]: return [0xCD]
    @property
    def size(self: Self) -> int: return 3
    def load(self: Self, opcode: int) -> None:
        super().load(opcode)
        self.nn = self._ram.get_word(self._registers.PC + 1)
    def __str__(self: Self) -> str:
        return f'{self._registers.PC:04X}; CALL 0x{self.nn:04X}'
    def handle(self: Self, opcode: int) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        nn = self._ram.get_word(self._registers.PC + 1)
        #PC = self._registers.PC + self.size()
        #self._ram[self._registers.SP - 2] = PC & 0xff
        #self._ram[self._registers.SP - 1] = (PC & 0xff00) >> 8
        #self._registers.SP -= 2
        #self._registers.PC = nn
        logging.debug(f'\t\t\t\t{self._registers.PC:04X}; CALL 0x{nn:04X}')

class DI(Instruction):
    @property
    def opcodes(self: Self) -> List[int]: return [0xF3]
    @property
    def size(self: Self) -> int: return 1
    def __str__(self: Self) -> str:
        return f'{self._registers.PC:04X}; DI\t; Disable interrupts.'
    def handle(self: Self, opcode: int) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        logging.debug(f'\t\t\t\t{self._registers.PC:04X}; Disable interrupts.')

class LD_dd_nn(Instruction):
    @property
    def opcodes(self: Self) -> List[int]:
        return [
            0b00_00_0001,	## BC
            0b00_01_0001,	## DE
            0b00_10_0001,	## HL
            0b00_11_0001,	## SP
        ]
    @property
    def size(self: Self) -> int: return 3
    def __str__(self: Self) -> str:
        return f'{self._registers.PC:04X}; {_dd2n[self.dd]} = 0x{self.nn:04X}'
    def load(self: Self, opcode: int) -> None:
        super().load(opcode)
        self.dd = (opcode >> 4) & 0x03
        self.nn = self._ram.get_word(self._registers.PC + 1)
    def execute(self: Self) -> None:
        self._registers.set_reg_dd(self.dd, self.nn)

class LD_deref_HL_n(Instruction):
    @property
    def opcodes(self: Self) -> List[int]: return [0x36]
    @property
    def size(self: Self) -> int: return 2
    def __str__(self: Self) -> str:
        return f'{self._registers.PC:04X}; *(HL) = *(0x{self._registers.HL:04X}) = 0x{self.n:02X}'
    def load(self: Self, opcode: int) -> None:
        super().load(opcode)
        self.n = self._ram.get_byte(self._registers.PC + 1)
    def execute(self: Self) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        self._ram[self._registers.HL] = self.n

class LD_deref_nn_A(Instruction):
    @property
    def opcodes(self: Self) -> List[int]: return [0x32]
    @property
    def size(self: Self) -> int: return 3
    def __str__(self: Self) -> str:
        return f'{self._registers.PC:04X}; *(0x{self.nn:04X}) := A (0x{self._registers.A:02X})'
    def load(self: Self, opcode: int) -> None:
        super().load(opcode)
        self.nn = self._ram.get_word(self._registers.PC + 1)
    def execute(self: Self) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        self._ram[self.nn] = self._registers.A

class LD_deref_nn_HL(Instruction):
    @property
    def opcodes(self: Self) -> List[int]: return [0x22]
    @property
    def size(self: Self) -> int: return 3
    def __str__(self: Self) -> str:
        return f'{self._registers.PC:04X}; *(0x{self.nn:04X}) := HL (0x{self._registers.HL:04X})'
    def load(self: Self, opcode: int) -> None:
        super().load(opcode)
        self.nn = self._ram.get_word(self._registers.PC + 1)
    def execute(self: Self) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        self._ram[self.nn + 0] = self._registers.L
        self._ram[self.nn + 1] = self._registers.H

class LD_r_n(Instruction):
    @property
    def opcodes(self: Self) -> List[int]: return [0x3E]
    @property
    def size(self: Self) -> int: return 2
    def load(self: Self, opcode: int) -> None:
        super().load(opcode)
        self.r = (opcode >> 3) & 0x07
        self.n = self._ram.get_byte(self._registers.PC + 1)
        self._registers.set_r_n(self.r, self.n)
    def __str__(self: Self) -> str:
        return f'{self._registers.PC:04X}; {_r2n[self.r]} = 0x{self.n:02X}'

class LDIR(Instruction):
    @property
    def opcodes(self: Self) -> List[int]: return [0xEDB0]
    @property
    def size(self: Self) -> int: return 2
    def load(self: Self, opcode: int) -> None:
        super().load(opcode)
    def __str__(self: Self) -> str:
        return f'{self._registers.PC:04X}; LDIR (DE=0x{self._registers.DE:04X}) <- (HL=0x{self._registers.HL:04X}), BC=0x{self._registers.BC:04X}'
    def handle(self: Self, opcode: int) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        ## FIXME

class IM_1(Instruction):
    @property
    def opcodes(self: Self) -> List[int]: return [0xED56]
    @property
    def size(self: Self) -> int: return 2
    def __str__(self: Self) -> str:
        return f'{self._registers.PC:04X}; IM 1\t; Use interrupt mode 1.'

class RET(Instruction):
    @property
    def opcodes(self: Self) -> List[int]: return [0xC9]
    @property
    def size(self: Self) -> int: return 1
    def handle(self: Self) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        logging.debug('Setting PC')
        self._registers.PC = self._ram[self._registers.SP]

class XOR_n(Instruction):
    @property
    def opcodes(self: Self) -> List[int]: return [0xEE]
    @property
    def size(self: Self) -> int: return 1
    def load(self: Self, opcode: int) -> None:
        super().load(opcode)
        self.n = self._ram.get_byte(self._registers.PC + 1)
    def __str__(self: Self) -> str:
        return f'{self._registers.PC:04X}; A ^= {self.n:02X}'

class XOR_r(Instruction):
    @property
    def opcodes(self: Self) -> List[int]:
      return [
          0b10101_000,	## B 0xA8
          0b10101_001,	## C 0xA9
          0b10101_010,	## D 0xAA
          0b10101_011,	## E 0xAB
          0b10101_100,	## H 0xAC
          0b10101_101,	## L 0xAD
          #0b10101_110,
          0b10101_111,	## A 0xAF
      ]
    @property
    def size(self: Self) -> int: return 1
    def load(self: Self, opcode: int) -> None:
        super().load(opcode)
        self.r = opcode & 0x07
        self.n = self._ram.get_byte(self._registers.PC + 1)
    def __str__(self: Self) -> str:
        if self.r == 0b111:
            return f'{self._registers.PC:04X}; A = 0, set flags.'
        return f'{self._registers.PC:04X}; A ^= {_r2n[self.r]}'
