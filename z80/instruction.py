import abc
import logging
import sys
from   typing import Self
import z80.ram
import z80.registers



instruction_set =\
[
    'CALL',
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
]

class Instruction(abc.ABC):
    def __init__(self: Self,
        registers: z80.registers.Registers,
        ram: z80.ram.RAM,
    ) -> None:
        self._registers = registers
        self._ram = ram
    
    @property
    @abc.abstractmethod
    def opcodes(self: Self) -> [int]: pass
    
    @property
    @abc.abstractmethod
    def size(self: Self) -> int: pass

    @abc.abstractmethod
    def handle(self: Self, opcode: int) -> None: pass



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

class CALL(Instruction):
    def opcodes(self: Self) -> [int]: return [0xCD]
    def size(self: Self) -> int: return 3
    def handle(self: Self, opcode: int) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        nn = self._ram.get_word(self._registers.PC + 1)
        PC = self._registers.PC + self.size()
        self._ram[self._registers.SP - 2] = PC & 0xff
        self._ram[self._registers.SP - 1] = (PC & 0xff00) >> 8
        self._registers.SP -= 2
        self._registers.PC = nn
        logging.debug(f'\t\t\t\t{self._registers.PC:04X}; CALL 0x{nn:04X}')

class DI(Instruction):
    def opcodes(self: Self) -> [int]: return [0xF3]
    def size(self: Self) -> int: return 1
    def handle(self: Self, opcode: int) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        logging.debug(f'\t\t\t\t{self._registers.PC:04X}; Disable interrupts.')

class LD_dd_nn(Instruction):
    def opcodes(self: Self) -> [int]:
        return [
            0b00_00_0001,	## BC
            0b00_01_0001,	## DE
            0b00_10_0001,	## HL
            0b00_11_0001,	## SP
        ]
    def size(self: Self) -> int: return 3
    def handle(self: Self, opcode: int) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        dd = (opcode >> 4) & 0x03
        nn = self._ram.get_word(self._registers.PC + 1)
        self._registers.set_reg_dd(dd, nn)
        logging.debug(f'\t\t\t\t{self._registers.PC:04X}; {_dd2n[dd]} = 0x{nn:04X}')

class LD_deref_HL_n(Instruction):
    def opcodes(self: Self) -> [int]: return [0x36]
    def size(self: Self) -> int: return 2
    def handle(self: Self, opcode: int) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        n = self._ram.get_byte(self._registers.PC + 1)
        self._ram[self._registers.HL] = n
        logging.debug(f'\t\t\t\t{self._registers.PC:04X}; *(HL) = *(0x{self._registers.HL:04X}) = 0x{n:02X}')

class LD_deref_nn_A(Instruction):
    def opcodes(self: Self) -> [int]: return [0x32]
    def size(self: Self) -> int: return 3
    def handle(self: Self, opcode: int) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        nn = self._ram.get_word(self._registers.PC + 1)
        self._ram[nn] = self._registers.A
        logging.debug(f'\t\t\t\t{self._registers.PC:04X}; *(0x{nn:04X}) := A (0x{self._registers.A:02X})')

class LD_deref_nn_HL(Instruction):
    def opcodes(self: Self) -> [int]: return [0x22]
    def size(self: Self) -> int: return 3
    def handle(self: Self, opcode: int) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        nn_L = self._ram.get_word(self._registers.PC + 1)
        nn_H = self._ram.get_word(self._registers.PC + 2)
        self._ram[nn_L] = self._registers.L
        self._ram[nn_H] = self._registers.H
        logging.debug(f'\t\t\t\t{self._registers.PC:04X}; *(0x{nn_L:04X}) := HL (0x{self._registers.HL:04X})')

class LD_r_n(Instruction):
    def opcodes(self: Self) -> [int]: return [0x3E]
    def size(self: Self) -> int: return 2
    def handle(self: Self, opcode: int) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        r = (opcode >> 3) & 0x07
        n = self._ram.get_byte(self._registers.PC + 1)
        self._registers.set_r_n(r, n)
        logging.debug(f'\t\t\t\t{self._registers.PC:04X}; {_r2n[r]} = 0x{n:02X}')

class LDIR(Instruction):
    def opcodes(self: Self) -> [int]: return [0xEDB0]
    def size(self: Self) -> int: return 2
    def handle(self: Self, opcode: int) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        logging.debug(f'\t\t\t\t{self._registers.PC:04X}; LDIR (DE=0x{self._registers.DE:04X}) <- (HL=0x{self._registers.HL:04X}), BC=0x{self._registers.BC:04X}')
        ## FIXME

class IM_1(Instruction):
    def opcodes(self: Self) -> [int]: return [0xED56]
    def size(self: Self) -> int: return 2
    def handle(self: Self, opcode: int) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        logging.debug(f'\t\t\t\tUse interrupt mode 1.')

class RET(Instruction):
    def opcodes(self: Self) -> [int]: return [0xC9]
    def size(self: Self) -> int: return 1
    def handle(self: Self) -> None:
        logging.debug(type(self).__name__ + '::' + sys._getframe().f_code.co_name)
        logging.debug('Setting PC')
        self._registers.PC = self._ram[self._registers.SP]
