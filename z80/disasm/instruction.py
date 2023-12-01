import logging
from   typing import Self
import z80.instructions

class AUX:
    routines =\
    {
        0x0056: 'FILVRM'
    }
    
    def add_routine(self: Self, address: int, routine_name: str) -> None:
        self.routines[address] = routine_name
    def get_routine(self: Self, address: int) -> str:
        return self.routines[address]
## Singleton
aux = AUX()



class CALL_nn(z80.instructions.CALL_nn):
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
    
    def __str__(self: Self) -> str:
        try:
            post = f', {aux.routines[self.nn]}()'
        except KeyError:
            post = ''
        
        return f'{self.PC:04X}; CALL 0x{self.nn:04X}{post}'

class DI(z80.instructions.DI):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; DI\t; Disable interrupts.'

class JP_nn(z80.instructions.JP_nn):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; JP 0x{self.nn:04X}'

class JR_e(z80.instructions.JR_e):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; JR 0x{self.PC+self.e+2:04X}\t; e={self.e}'

class LD_dd_nn(z80.instructions.LD_dd_nn):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; {self.dd2n(self.dd)} = 0x{self.nn:04X}'
    def execute(self: Self):
        self._registers.set_reg_dd(self.dd, self.nn)

class LD_deref_HL_n(z80.instructions.LD_deref_HL_n):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; *(HL) = *(0x{self._registers.HL:04X}) = 0x{self.n:02X}'

class LD_deref_nn_A(z80.instructions.LD_deref_nn_A):
    def __str__(self: Self) -> str:
        comment = ''
        if self.nn == 0xFD9A:
            comment = 'H.KEYI[0] = A, 0xC3 means "JP"'
        return f'{self.PC:04X}; *(0x{self.nn:04X}) := A (0x{self._registers.A:02X})' + (
            (' ' + comment) if comment else comment)

class LD_deref_nn_HL(z80.instructions.LD_deref_nn_HL):
    def __str__(self: Self) -> str:
        comment = ''
        if self.nn == 0xFD9B:
            comment = 'H.KEYI[1] = L, H.KEYI[2] = H'
        return f'{self.PC:04X}; *(0x{self.nn:04X}) := HL (0x{self._registers.HL:04X})' + (
            (' ' + comment) if comment else comment)
    def execute(self: Self) -> None:
        self._ram[self.nn+0] = self._registers.L
        self._ram[self.nn+1] = self._registers.H

class LD_r_n(z80.instructions.LD_r_n):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; {self.r2n(self.r)} = 0x{self.n:02X}'
    def execute(self: Self):
        self._registers.set_r_n(self.r, self.n)

class LD_r_rprime(z80.instructions.LD_r_rprime):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; {self.r2n(self.r)} = {self.r2n(self.rprime)}'

class LDIR(z80.instructions.LDIR):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; LDIR (DE=0x{self._registers.DE:04X}) <- (HL=0x{self._registers.HL:04X}), BC=0x{self._registers.BC:04X}'

class IM_1(z80.instructions.IM_1):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; IM 1\t; Use interrupt mode 1.'

class RET(z80.instructions.RET):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; RET'

class XOR_n(z80.instructions.XOR_n):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; A ^= {self.n:02X}'

class XOR_rprime(z80.instructions.XOR_rprime):
    def __str__(self: Self) -> str:
        if self.rprime == 0b111:
            return f'{self.PC:04X}; A = 0, set flags.'
        return f'{self.PC:04X}; A ^= {self.r2n(self.rprime)}'
