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



class ADC_A_deref_HL(z80.instructions.ADC_A_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class ADC_A_deref_IX_plus_d(z80.instructions.ADC_A_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class ADC_A_deref_IY_plus_d(z80.instructions.ADC_A_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class ADC_A_n(z80.instructions.ADC_A_n):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class ADC_A_r(z80.instructions.ADC_A_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class ADC_HL_ss(z80.instructions.ADC_HL_ss):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class ADD_A_deref_HL(z80.instructions.ADD_A_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class ADD_A_deref_IX_plus_d(z80.instructions.ADD_A_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class ADD_A_deref_IY_plus_d(z80.instructions.ADD_A_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class ADD_A_n(z80.instructions.ADD_A_n):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class ADD_A_r(z80.instructions.ADD_A_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class ADD_HL_ss(z80.instructions.ADD_HL_ss):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; ADD HL {self.ssn}\t; HL += {self.ssn}'

class ADD_IX_pp(z80.instructions.ADD_IX_pp):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class ADD_IY_rr(z80.instructions.ADD_IY_rr):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class AND_deref_HL(z80.instructions.AND_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class AND_deref_IX_plus_d(z80.instructions.AND_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class AND_deref_IY_plus_d(z80.instructions.AND_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class AND_n(z80.instructions.AND_n):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; AND 0x{self.n:02X}\t; A &= {self.n:09_b}'

class AND_r(z80.instructions.AND_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class BIT_b_deref_HL(z80.instructions.BIT_b_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class BIT_b_deref_IX_plus_d(z80.instructions.BIT_b_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class BIT_b_deref_IY_plus_d(z80.instructions.BIT_b_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class BIT_b_r(z80.instructions.BIT_b_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class CALL_cc_nn(z80.instructions.CALL_cc_nn):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class CALL_nn(z80.instructions.CALL_nn):
    def __str__(self: Self) -> str:
        try:
            post = f', {aux.routines[self.nn]}'
        except KeyError:
            post = ''
        
        return f'{self.PC:04X}; CALL 0x{self.nn:04X}{post}'

class CCF(z80.instructions.CCF):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class CPD(z80.instructions.CPD):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class CPDR(z80.instructions.CPDR):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class CPI(z80.instructions.CPI):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class CPIR(z80.instructions.CPIR):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class CPL(z80.instructions.CPL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class CP_deref_HL(z80.instructions.CP_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class CP_deref_IX_plus_d(z80.instructions.CP_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class CP_deref_IY_plus_d(z80.instructions.CP_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class CP_n(z80.instructions.CP_n):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class CP_r(z80.instructions.CP_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class DAA(z80.instructions.DAA):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class DEC_deref_HL(z80.instructions.DEC_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class DEC_deref_IX_plus_d(z80.instructions.DEC_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class DEC_deref_IY_plus_d(z80.instructions.DEC_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class DEC_IX(z80.instructions.DEC_IX):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class DEC_IY(z80.instructions.DEC_IY):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class DEC_r(z80.instructions.DEC_r):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; DEC {self.rn}\t\t; --{self.rn}'

class DEC_ss(z80.instructions.DEC_ss):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class DI(z80.instructions.DI):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; {self.name()}\t; Disable interrupts.'

class DJNZ_e(z80.instructions.DJNZ_e):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; DJNZ 0x{self.jump_destination:04X}\t;'

class EI(z80.instructions.EI):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class EXX(z80.instructions.EXX):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class EX_AF_AFprime(z80.instructions.EX_AF_AFprime):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; {self.name()}\t;'

class EX_deref_SP_HL(z80.instructions.EX_deref_SP_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class EX_deref_SP_IX(z80.instructions.EX_deref_SP_IX):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class EX_deref_SP_IY(z80.instructions.EX_deref_SP_IY):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class EX_DE_HL(z80.instructions.EX_DE_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; {self.name()}\t;'

class HALT(z80.instructions.HALT):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class IM_0(z80.instructions.IM_0):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class IM_1(z80.instructions.IM_1):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class IM_2(z80.instructions.IM_2):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class INC_deref_HL(z80.instructions.INC_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class INC_deref_IX_plus_d(z80.instructions.INC_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class INC_deref_IY_plus_d(z80.instructions.INC_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class INC_IX(z80.instructions.INC_IX):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class INC_IY(z80.instructions.INC_IY):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class INC_r(z80.instructions.INC_r):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; INC {self.rn}\t\t; ++{self.rn}'

class INC_ss(z80.instructions.INC_ss):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; INC {self.ssn}\t\t; ++{self.ssn}'

class IND(z80.instructions.IND):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class INDR(z80.instructions.INDR):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class INI(z80.instructions.INI):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class INIR(z80.instructions.INIR):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class IN_A_deref_n(z80.instructions.IN_A_deref_n):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class IN_r_deref_C(z80.instructions.IN_r_deref_C):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class JP_cc_nn(z80.instructions.JP_cc_nn):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class JP_deref_HL(z80.instructions.JP_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class JP_nn(z80.instructions.JP_nn):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; JP 0x{self.nn:04X}'

class JR_C_e(z80.instructions.JR_C_e):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class JR_e(z80.instructions.JR_e):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; JR 0x{self.jump_destination:04X}\t;'

class JR_NC_e(z80.instructions.JR_NC_e):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class JR_NZ_e(z80.instructions.JR_NZ_e):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; JR NZ 0x{self.jump_destination:04X}\t;'

class JR_Z_e(z80.instructions.JR_Z_e):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LDD(z80.instructions.LDD):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LDDR(z80.instructions.LDDR):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LDI(z80.instructions.LDI):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LDIR(z80.instructions.LDIR):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_A_deref_BC(z80.instructions.LD_A_deref_BC):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_A_deref_DE(z80.instructions.LD_A_deref_DE):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_A_deref_nn(z80.instructions.LD_A_deref_nn):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_A_I(z80.instructions.LD_A_I):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_A_R(z80.instructions.LD_A_R):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_dd_deref_nn(z80.instructions.LD_dd_deref_nn):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; {self.ddn} = *(0x{self.nn:04X})'
    def execute(self: Self):
        self._registers.set_reg_dd(self.dd, self.nn)

class LD_dd_nn(z80.instructions.LD_dd_nn):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; LD {self.ddn}, 0x{self.nn:04X}\t; {self.ddn} = 0x{self.nn:04X}'
    def execute(self: Self):
        self._registers.set_reg_dd(self.dd, self.nn)

class LD_deref_BC_A(z80.instructions.LD_deref_BC_A):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_deref_DE_A(z80.instructions.LD_deref_DE_A):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_deref_HL_n(z80.instructions.LD_deref_HL_n):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; LD (HL), 0x{self.n:02X}\t; *(HL) = *(0x{self._registers.HL:04X}) = 0x{self.n:02X}'

class LD_deref_HL_r(z80.instructions.LD_deref_HL_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_deref_IX_plus_d_n(z80.instructions.LD_deref_IX_plus_d_n):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_deref_IX_plus_d_r(z80.instructions.LD_deref_IX_plus_d_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_deref_IY_plus_d_n(z80.instructions.LD_deref_IY_plus_d_n):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_deref_IY_plus_d_r(z80.instructions.LD_deref_IY_plus_d_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_deref_nn_A(z80.instructions.LD_deref_nn_A):
    def __str__(self: Self) -> str:
        comment = ''
        if self.nn == 0xFD9A:
            comment = 'H.KEYI[0] = A, 0xC3 means "JP"'
        return f'{self.PC:04X}; *(0x{self.nn:04X}) := A (0x{self._registers.A:02X})' + (
            (' ' + comment) if comment else comment)

class LD_deref_nn_dd(z80.instructions.LD_deref_nn_dd):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

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

class LD_deref_nn_IX(z80.instructions.LD_deref_nn_IX):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_HL_deref_nn(z80.instructions.LD_HL_deref_nn):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_IX_deref_nn(z80.instructions.LD_IX_deref_nn):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_IX_nn(z80.instructions.LD_IX_nn):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_IY_deref_nn(z80.instructions.LD_IY_deref_nn):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_IY_nn(z80.instructions.LD_IY_nn):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_I_A(z80.instructions.LD_I_A):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_R_A(z80.instructions.LD_R_A):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_r_deref_HL(z80.instructions.LD_r_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_r_deref_IX_plus_d(z80.instructions.LD_r_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_r_deref_IY_plus_d(z80.instructions.LD_r_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_r_n(z80.instructions.LD_r_n):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; LD {self.rn}, 0x{self.n:02X}\t; {self.rn} = 0x{self.n:02X}'
    def execute(self: Self):
        self._registers.set_r_n(self.r, self.n)

class LD_r_rprime(z80.instructions.LD_r_rprime):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; LD {self.rn}, {self.rprimen}\t\t; {self.rn} = {self.rprimen}'

class LD_SP_HL(z80.instructions.LD_SP_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_SP_IX(z80.instructions.LD_SP_IX):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_SP_IY(z80.instructions.LD_SP_IY):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class NEG(z80.instructions.NEG):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class NOP(z80.instructions.NOP):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class OR_deref_HL(z80.instructions.OR_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class OR_deref_IX_plus_d(z80.instructions.OR_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class OR_deref_IY_plus_d(z80.instructions.OR_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class OR_n(z80.instructions.OR_n):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class OR_r(z80.instructions.OR_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class OTDR(z80.instructions.OTDR):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class OTIR(z80.instructions.OTIR):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class OUTD(z80.instructions.OUTD):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class OUTI(z80.instructions.OUTI):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class OUT_deref_C_r(z80.instructions.OUT_deref_C_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class OUT_deref_n_A(z80.instructions.OUT_deref_n_A):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class POP_IX(z80.instructions.POP_IX):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class POP_IY(z80.instructions.POP_IY):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class POP_qq(z80.instructions.POP_qq):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; POP {self.qqn}\t\t;'

class PUSH_IX(z80.instructions.PUSH_IX):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class PUSH_IY(z80.instructions.PUSH_IY):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class PUSH_qq(z80.instructions.PUSH_qq):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RET(z80.instructions.RET):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; {self.name()}\t\t;'

class RETI(z80.instructions.RETI):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RETN(z80.instructions.RETN):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RET_cc(z80.instructions.RET_cc):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RLA(z80.instructions.RLA):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RLCA(z80.instructions.RLCA):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RLC_deref_HL(z80.instructions.RLC_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RLC_deref_IX_plus_d(z80.instructions.RLC_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RLC_r(z80.instructions.RLC_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RL_deref_HL(z80.instructions.RL_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RL_deref_IX_plus_d(z80.instructions.RL_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RL_deref_IY_plus_d(z80.instructions.RL_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RL_r(z80.instructions.RL_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RRA(z80.instructions.RRA):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RRCA(z80.instructions.RRCA):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RR_deref_HL(z80.instructions.RR_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RR_deref_IX_plus_d(z80.instructions.RR_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RR_deref_IY_plus_d(z80.instructions.RR_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RR_r(z80.instructions.RR_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class RST_p(z80.instructions.RST_p):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SBC_HL_ss(z80.instructions.SBC_HL_ss):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SCF(z80.instructions.SCF):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SET_b_deref_HL(z80.instructions.SET_b_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SET_b_deref_IX_plus_d(z80.instructions.SET_b_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SET_b_deref_IY_plus_d(z80.instructions.SET_b_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SET_b_r(z80.instructions.SET_b_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SLA_deref_HL(z80.instructions.SLA_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SLA_deref_IX_plus_d(z80.instructions.SLA_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SLA_deref_IY_plus_d(z80.instructions.SLA_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SLA_r(z80.instructions.SLA_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SRL_deref_HL(z80.instructions.SRL_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SRL_deref_IX_plus_d(z80.instructions.SRL_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SRL_deref_IY_plus_d(z80.instructions.SRL_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SRL_r(z80.instructions.SRL_r):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SUB_deref_HL(z80.instructions.SUB_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SUB_deref_IX_plus_d(z80.instructions.SUB_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SUB_deref_IY_plus_d(z80.instructions.SUB_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SUB_n(z80.instructions.SUB_n):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class SUB_r(z80.instructions.SUB_r):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; SUB {self.rn}\t\t; A -= {self.rn}'

class XOR_deref_HL(z80.instructions.XOR_deref_HL):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class XOR_deref_IX_plus_d(z80.instructions.XOR_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class XOR_deref_IY_plus_d(z80.instructions.XOR_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class XOR_n(z80.instructions.XOR_n):
    def __str__(self: Self) -> str:
        return f'{self.PC:04X}; A ^= {self.n:02X}'

class XOR_rprime(z80.instructions.XOR_rprime):
    def __str__(self: Self) -> str:
        if self.rprime == 0b111:
            return f'{self.PC:04X}; A = 0, set flags.'
        return f'{self.PC:04X}; A ^= {self.rprimen}'
