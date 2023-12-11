import logging
from   typing import Self, List
import z80.instruction
import z80.instructions

z80.instruction.Instruction.set_PC_formatter(func=lambda instr: f'{instr.PC:04x}')



class ADC_A_deref_HL(z80.instructions.ADC_A_deref_HL):
    def __str__(self: Self) -> str:
        return f'\tadc a,(hl)\t\t\t;{self.formatted_PC}'

class ADC_A_deref_IX_plus_d(z80.instructions.ADC_A_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\tadc a,(ix+0{self.d:02x}h)\t\t\t;{self.formatted_PC}'

class ADC_A_deref_IY_plus_d(z80.instructions.ADC_A_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\tadc a,(iy+0{self.d:02x}h)\t\t\t;{self.formatted_PC}'

class ADC_A_n(z80.instructions.ADC_A_n):
    def __str__(self: Self) -> str:
        return f'\tadc a,0{self.n:02x}h\t\t;{self.formatted_PC}'

class ADC_A_r(z80.instructions.ADC_A_r):
    def __str__(self: Self) -> str:
        return f'\tadc a,{self.r.lower()}\t\t\t;{self.formatted_PC}'

class ADC_HL_ss(z80.instructions.ADC_HL_ss):
    def __str__(self: Self) -> str:
        return f'\tadc hl,{self.ss.lower()}\t\t\t;{self.formatted_PC}'

class ADD_A_deref_HL(z80.instructions.ADD_A_deref_HL):
    def __str__(self: Self) -> str:
        return f'\tadd a,(hl)\t\t\t;{self.formatted_PC}'

class ADD_A_deref_IX_plus_d(z80.instructions.ADD_A_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\tadd a,(ix+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class ADD_A_deref_IY_plus_d(z80.instructions.ADD_A_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\tadd a,(iy+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class ADD_A_n(z80.instructions.ADD_A_n):
    def __str__(self: Self) -> str:
        return f'\tadd a,0{self.n:02x}h\t\t;{self.formatted_PC}'

class ADD_A_r(z80.instructions.ADD_A_r):
    def __str__(self: Self) -> str:
        return f'\tadd a,{self.r.lower()}\t\t\t;{self.formatted_PC}'

class ADD_HL_ss(z80.instructions.ADD_HL_ss):
    def __str__(self: Self) -> str:
        return f'\tadd hl,{self.ss.lower()}\t\t\t;{self.formatted_PC}'

class ADD_IX_pp(z80.instructions.ADD_IX_pp):
    def __str__(self: Self) -> str:
        return f'\tadd ix,{self.pp.lower()}\t\t;{self.formatted_PC}'

class ADD_IY_rr(z80.instructions.ADD_IY_rr):
    def __str__(self: Self) -> str:
        return f'\tadd iy,{self.rr.lower()}\t\t;{self.formatted_PC}'

class AND_deref_HL(z80.instructions.AND_deref_HL):
    def __str__(self: Self) -> str:
        return f'\tand (hl)\t\t\t;{self.formatted_PC}'

class AND_deref_IX_plus_d(z80.instructions.AND_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\tand (ix+0{self.d:02x}h)\t\t\t;{self.formatted_PC}'

class AND_deref_IY_plus_d(z80.instructions.AND_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\tand (iy+0{self.d:02x}h)\t\t\t;{self.formatted_PC}'

class AND_n(z80.instructions.AND_n):
    def __str__(self: Self) -> str:
        return f'\tand 0{self.n:02x}h\t\t;{self.formatted_PC}'

class AND_r(z80.instructions.AND_r):
    def __str__(self: Self) -> str:
        return f'\tand {self.r.lower()}\t\t\t;{self.formatted_PC}'

class BIT_b_deref_HL(z80.instructions.BIT_b_deref_HL):
    def __str__(self: Self) -> str:
        return f'\tbit {self.b},(hl)\t\t;{self.formatted_PC}'

class BIT_b_deref_IX_plus_d(z80.instructions.BIT_b_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\tbit {self.b},(ix+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class BIT_b_deref_IY_plus_d(z80.instructions.BIT_b_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\tbit {self.b},(iy+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class BIT_b_r(z80.instructions.BIT_b_r):
    def __str__(self: Self) -> str:
        return f'\tbit {self.b},{self.r.lower()}\t\t;{self.formatted_PC}'

class CALL_cc_nn(z80.instructions.CALL_cc_nn):
    def __str__(self: Self) -> str:
        return f'\tcall {self.cc.lower()},0{self.nn:04x}h\t\t;{self.formatted_PC}'

class CALL_nn(z80.instructions.CALL_nn):
    def __str__(self: Self) -> str:
        return f'\tcall 0{self.nn:04x}h\t\t;{self.formatted_PC}'

class CCF(z80.instructions.CCF):
    def __str__(self: Self) -> str:
        return f'\tccf\t\t\t;{self.formatted_PC}'

class CPD(z80.instructions.CPD):
    def __str__(self: Self) -> str:
        return f'\tcpd\t\t\t;{self.formatted_PC}'

class CPDR(z80.instructions.CPDR):
    def __str__(self: Self) -> str:
        return f'\tcpdr\t\t\t;{self.formatted_PC}'

class CPI(z80.instructions.CPI):
    def __str__(self: Self) -> str:
        return f'\tcpi\t\t\t;{self.formatted_PC}'

class CPIR(z80.instructions.CPIR):
    def __str__(self: Self) -> str:
        return f'\tcpir\t\t\t;{self.formatted_PC}'

class CPL(z80.instructions.CPL):
    def __str__(self: Self) -> str:
        return f'\tcpl\t\t\t;{self.formatted_PC}'

class CP_deref_HL(z80.instructions.CP_deref_HL):
    def __str__(self: Self) -> str:
        return f'\tcp (hl)\t\t\t;{self.formatted_PC}'

class CP_deref_IX_plus_d(z80.instructions.CP_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\tcp (ix+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class CP_deref_IY_plus_d(z80.instructions.CP_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\tcp (iy+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class CP_n(z80.instructions.CP_n):
    def __str__(self: Self) -> str:
        return f'\tcp 0{self.n:02x}h\t\t;{self.formatted_PC}'

class CP_r(z80.instructions.CP_r):
    def __str__(self: Self) -> str:
        return f'\tcp {self.r.lower()}\t\t\t;{self.formatted_PC}'

class DAA(z80.instructions.DAA):
    def __str__(self: Self) -> str:
        return f'\tdaa\t\t\t;{self.formatted_PC}'

class DEC_deref_HL(z80.instructions.DEC_deref_HL):
    def __str__(self: Self) -> str:
        return f'\tdec (hl)\t\t\t;{self.formatted_PC}'

class DEC_deref_IX_plus_d(z80.instructions.DEC_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\tdec (ix+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class DEC_deref_IY_plus_d(z80.instructions.DEC_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\tdec (iy+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class DEC_IX(z80.instructions.DEC_IX):
    def __str__(self: Self) -> str:
        return f'\tdec ix\t\t;{self.formatted_PC}'

class DEC_IY(z80.instructions.DEC_IY):
    def __str__(self: Self) -> str:
        return f'\tdec iy\t\t;{self.formatted_PC}'

class DEC_r(z80.instructions.DEC_r):
    def __str__(self: Self) -> str:
        return f'\tdec {self.r.lower()}\t\t\t;{self.formatted_PC}'

class DEC_ss(z80.instructions.DEC_ss):
    def __str__(self: Self) -> str:
        return f'\tdec {self.ss.lower()}\t\t\t;{self.formatted_PC}'

class DI(z80.instructions.DI):
    def __str__(self: Self) -> str:
        return f'\tdi\t\t\t;{self.formatted_PC}'

class DJNZ_e(z80.instructions.DJNZ_e):
    def __str__(self: Self) -> str:
        return f'\tdjnz ${self.e+2:+}\t\t;{self.formatted_PC}'

class EI(z80.instructions.EI):
    def __str__(self: Self) -> str:
        return f'\tei\t\t\t;{self.formatted_PC}'

class EXX(z80.instructions.EXX):
    def __str__(self: Self) -> str:
        return f'\texx\t\t\t;{self.formatted_PC}'

class EX_AF_AFprime(z80.instructions.EX_AF_AFprime):
    def __str__(self: Self) -> str:
        return f"\tex af,af'\t\t\t;{self.formatted_PC}"

class EX_deref_SP_HL(z80.instructions.EX_deref_SP_HL):
    def __str__(self: Self) -> str:
        return f"\tex (sp),hl\t\t\t;{self.formatted_PC}"

class EX_deref_SP_IX(z80.instructions.EX_deref_SP_IX):
    def __str__(self: Self) -> str:
        return f"\tex (sp),ix\t\t\t;{self.formatted_PC}"

class EX_deref_SP_IY(z80.instructions.EX_deref_SP_IY):
    def __str__(self: Self) -> str:
        return f"\tex (sp),iy\t\t\t;{self.formatted_PC}"

class EX_DE_HL(z80.instructions.EX_DE_HL):
    def __str__(self: Self) -> str:
        return f'\tex de,hl\t\t\t;{self.formatted_PC}'

class HALT(z80.instructions.HALT):
    def __str__(self: Self) -> str:
        return f'\thalt\t\t\t;{self.formatted_PC}'

#class Illegal(z80.instruction.Illegal):
#    def __str__(self: Self) -> str:
#        return f'\t???????\t\t;{self.formatted_PC}'

class IM_0(z80.instructions.IM_0):
    def __str__(self: Self) -> str:
        return f'\tim 0\t\t;{self.formatted_PC}'

class IM_1(z80.instructions.IM_1):
    def __str__(self: Self) -> str:
        return f'\tim 1\t\t;{self.formatted_PC}'

class IM_2(z80.instructions.IM_2):
    def __str__(self: Self) -> str:
        return f'\tim 2\t\t;{self.formatted_PC}'

class INC_deref_HL(z80.instructions.INC_deref_HL):
    def __str__(self: Self) -> str:
        return f'\tinc (hl)\t\t\t;{self.formatted_PC}'

class INC_deref_IX_plus_d(z80.instructions.INC_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\tinc (ix+0{self.d:02x}h)\t\t\t;{self.formatted_PC}'

class INC_deref_IY_plus_d(z80.instructions.INC_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\tinc (iy+0{self.d:02x}h)\t\t\t;{self.formatted_PC}'

class INC_IX(z80.instructions.INC_IX):
    def __str__(self: Self) -> str:
        return f'\tinc ix\t\t\t;{self.formatted_PC}'

class INC_IY(z80.instructions.INC_IY):
    def __str__(self: Self) -> str:
        return f'\tinc iy\t\t\t;{self.formatted_PC}'

class INC_r(z80.instructions.INC_r):
    def __str__(self: Self) -> str:
        return f'\tinc {self.r.lower()}\t\t\t;{self.formatted_PC}'

class INC_ss(z80.instructions.INC_ss):
    def __str__(self: Self) -> str:
        return f'\tinc {self.ss.lower()}\t\t\t;{self.formatted_PC}'

class IND(z80.instructions.IND):
    def __str__(self: Self) -> str:
        return f'\tind\t\t\t;{self.formatted_PC}'

class INDR(z80.instructions.INDR):
    def __str__(self: Self) -> str:
        return f'\tindr\t\t\t;{self.formatted_PC}'

class INI(z80.instructions.INI):
    def __str__(self: Self) -> str:
        return f'\tini\t\t\t;{self.formatted_PC}'

class INIR(z80.instructions.INIR):
    def __str__(self: Self) -> str:
        return f'\tinir\t\t\t;{self.formatted_PC}'

class IN_A_deref_n(z80.instructions.IN_A_deref_n):
    def __str__(self: Self) -> str:
        return f'\tin a,(0{self.n:02x}h)\t\t;{self.formatted_PC}'

class IN_r_deref_C(z80.instructions.IN_r_deref_C):
    def __str__(self: Self) -> str:
        return f'\tin {self.r.lower()},(c)\t\t;{self.formatted_PC}'

class JP_cc_nn(z80.instructions.JP_cc_nn):
    def __str__(self: Self) -> str:
        return f'\tjp {self.cc.lower()},0{self.nn:04x}h\t\t;{self.formatted_PC}'

class JP_deref_HL(z80.instructions.JP_deref_HL):
    def __str__(self: Self) -> str:
        return f'\tjp (hl)\t\t\t;{self.formatted_PC}'

class JP_nn(z80.instructions.JP_nn):
    def __str__(self: Self) -> str:
        return f'\tjp 0{self.nn:04x}h\t\t;{self.formatted_PC}'

class JR_C_e(z80.instructions.JR_C_e):
    def __str__(self: Self) -> str:
        return f'\tjr c,${self.e+2:+}\t\t;{self.formatted_PC}'

class JR_e(z80.instructions.JR_e):
    def __str__(self: Self) -> str:
        return f'\tjr ${self.e+2:+}\t\t;{self.formatted_PC}'

class JR_NC_e(z80.instructions.JR_NC_e):
    def __str__(self: Self) -> str:
        return f'\tjr nc,${self.e+2:+}\t\t;{self.formatted_PC}'

class JR_NZ_e(z80.instructions.JR_NZ_e):
    def __str__(self: Self) -> str:
        return f'\tjr nz,${self.e+2:+}\t\t;{self.formatted_PC}'

class JR_Z_e(z80.instructions.JR_Z_e):
    def __str__(self: Self) -> str:
        return f'\tjr z,${self.e+2:+}\t\t;{self.formatted_PC}'

class LDD(z80.instructions.LDD):
    def __str__(self: Self) -> str:
        return f'\tldd\t\t\t;{self.formatted_PC}'

class LDDR(z80.instructions.LDDR):
    def __str__(self: Self) -> str:
        return f'\tlddr\t\t;{self.formatted_PC}'

class LDI(z80.instructions.LDI):
    def __str__(self: Self) -> str:
        return f'\tldi\t\t;{self.formatted_PC}'

class LDIR(z80.instructions.LDIR):
    def __str__(self: Self) -> str:
        return f'\tldir\t\t;{self.formatted_PC}'

class LD_A_deref_BC(z80.instructions.LD_A_deref_BC):
    def __str__(self: Self) -> str:
        return f'\tld a,(bc)\t\t\t;{self.formatted_PC}'

class LD_A_deref_DE(z80.instructions.LD_A_deref_DE):
    def __str__(self: Self) -> str:
        return f'\tld a,(de)\t\t\t;{self.formatted_PC}'

class LD_A_deref_nn(z80.instructions.LD_A_deref_nn):
    def __str__(self: Self) -> str:
        return f'\tld a,(0{self.nn:04x}h)\t\t;{self.formatted_PC}'

class LD_A_I(z80.instructions.LD_A_I):
    def __str__(self: Self) -> str:
        return f'\tld a,i\t\t;{self.formatted_PC}'

class LD_A_R(z80.instructions.LD_A_R):
    def __str__(self: Self) -> str:
        return f'\tld a,r\t\t;{self.formatted_PC}'

class LD_dd_deref_nn(z80.instructions.LD_dd_deref_nn):
    def __str__(self: Self) -> str:
        return f'\tld {self.dd.lower()},(0{self.nn:04x}h)\t\t;{self.formatted_PC}'

class LD_dd_nn(z80.instructions.LD_dd_nn):
    def __str__(self: Self) -> str:
        return f'\tld {self.dd.lower()},0{self.nn:04x}h\t\t;{self.formatted_PC}'
    def execute(self: Self):
        self._registers.set_reg_dd(self._dd, self.nn)

class LD_deref_BC_A(z80.instructions.LD_deref_BC_A):
    def __str__(self: Self) -> str:
        return f'\tld (bc),a\t\t\t;{self.formatted_PC}'

class LD_deref_DE_A(z80.instructions.LD_deref_DE_A):
    def __str__(self: Self) -> str:
        return f'\tld (de),a\t\t\t;{self.formatted_PC}'

class LD_deref_HL_n(z80.instructions.LD_deref_HL_n):
    def __str__(self: Self) -> str:
        return f'\tld (hl),0{self.n:02x}h\t\t;{self.formatted_PC}'

class LD_deref_HL_r(z80.instructions.LD_deref_HL_r):
    def __str__(self: Self) -> str:
        return f'\tld (hl),{self.r.lower()}\t\t\t;{self.formatted_PC}'

class LD_deref_IX_plus_d_n(z80.instructions.LD_deref_IX_plus_d_n):
    def __str__(self: Self) -> str:
        return f'\tld (ix+0{self.d:02x}h),0{self.n:02x}h\t\t;{self.formatted_PC}'

class LD_deref_IX_plus_d_r(z80.instructions.LD_deref_IX_plus_d_r):
    def __str__(self: Self) -> str:
        return f'\tld (ix+0{self.d:02x}h),{self.r.lower()}\t\t;{self.formatted_PC}'

class LD_deref_IY_plus_d_n(z80.instructions.LD_deref_IY_plus_d_n):
    def __str__(self: Self) -> str:
        return f'\tld (iy+0{self.d:02x}h),0{self.n:02x}h\t\t;{self.formatted_PC}'

class LD_deref_IY_plus_d_r(z80.instructions.LD_deref_IY_plus_d_r):
    def __str__(self: Self) -> str:
        return f'\tld (iy+0{self.d:02x}h),{self.r.lower()}\t\t;{self.formatted_PC}'

class LD_deref_nn_A(z80.instructions.LD_deref_nn_A):
    def __str__(self: Self) -> str:
        return f'\tld (0{self.nn:04x}h),a\t\t;{self.formatted_PC}'

class LD_deref_nn_dd(z80.instructions.LD_deref_nn_dd):
    def __str__(self: Self) -> str:
        return f'\tld (0{self.nn:04x}h),{self.dd.lower()}\t\t;{self.formatted_PC}'

class LD_deref_nn_HL(z80.instructions.LD_deref_nn_HL):
    def __str__(self: Self) -> str:
        return f'\tld (0{self.nn:04x}h),hl\t\t;{self.formatted_PC}'
    def execute(self: Self) -> None:
        self._ram.set_word(offset=self.nn, value=self._registers.HL)

class LD_deref_nn_IX(z80.instructions.LD_deref_nn_IX):
    def __str__(self: Self) -> str:
        return f'\tld (0{self.nn:04x}h),ix\t\t;{self.formatted_PC}'

class LD_HL_deref_nn(z80.instructions.LD_HL_deref_nn):
    def __str__(self: Self) -> str:
        return f'\tld hl,(0{self.nn:04x}h)\t\t;{self.formatted_PC}'

class LD_IX_deref_nn(z80.instructions.LD_IX_deref_nn):
    def __str__(self: Self) -> str:
        return f'\tld ix,(0{self.nn:04x}h)\t\t;{self.formatted_PC}'

class LD_IX_nn(z80.instructions.LD_IX_nn):
    def __str__(self: Self) -> str:
        return f'\tld ix,0{self.nn:04x}h\t\t;{self.formatted_PC}'

class LD_IY_deref_nn(z80.instructions.LD_IY_deref_nn):
    def __str__(self: Self) -> str:
        return f'\tld iy,(0{self.nn:04x}h)\t\t;{self.formatted_PC}'

class LD_IY_nn(z80.instructions.LD_IY_nn):
    def __str__(self: Self) -> str:
        return f'\tld iy,0{self.nn:04x}h\t\t;{self.formatted_PC}'

class LD_I_A(z80.instructions.LD_I_A):
    def __str__(self: Self) -> str:
        return f'\tld i,a\t\t\t;{self.formatted_PC}'

class LD_R_A(z80.instructions.LD_R_A):
    def __str__(self: Self) -> str:
        return f'\tld r,a\t\t\t;{self.formatted_PC}'

class LD_r_deref_HL(z80.instructions.LD_r_deref_HL):
    def __str__(self: Self) -> str:
        return f'\tld {self.r.lower()},(hl)\t\t\t;{self.formatted_PC}'

class LD_r_deref_IX_plus_d(z80.instructions.LD_r_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\tld {self.r.lower()},(ix+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class LD_r_deref_IY_plus_d(z80.instructions.LD_r_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\tld {self.r.lower()},(iy+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class LD_r_n(z80.instructions.LD_r_n):
    def __str__(self: Self) -> str:
        return f'\tld {self.r.lower()},0{self.n:02x}h\t\t;{self.formatted_PC}'

class LD_r_rprime(z80.instructions.LD_r_rprime):
    def __str__(self: Self) -> str:
        return f'\tld {self.r.lower()},{self.rprime.lower()}\t\t\t;{self.formatted_PC}'

class LD_SP_HL(z80.instructions.LD_SP_HL):
    def __str__(self: Self) -> str:
        return f'\tld sp,hl\t\t\t;{self.formatted_PC}'

class LD_SP_IX(z80.instructions.LD_SP_IX):
    def __str__(self: Self) -> str:
        return f'\tld sp,ix\t\t\t;{self.formatted_PC}'

class LD_SP_IY(z80.instructions.LD_SP_IY):
    def __str__(self: Self) -> str:
        return f'\tld sp,iy\t\t\t;{self.formatted_PC}'

class NEG(z80.instructions.NEG):
    def __str__(self: Self) -> str:
        return f'\tneg\t\t;{self.formatted_PC}'

class NOP(z80.instructions.NOP):
    def __str__(self: Self) -> str:
        return f'\tnop\t\t\t;{self.formatted_PC}'

class OR_deref_HL(z80.instructions.OR_deref_HL):
    def __str__(self: Self) -> str:
        return f'\tor (hl)\t\t\t;{self.formatted_PC}'

class OR_deref_IX_plus_d(z80.instructions.OR_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\tor (ix+0{self.d:02x}h)\t\t\t;{self.formatted_PC}'

class OR_deref_IY_plus_d(z80.instructions.OR_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\tor (iy+0{self.d:02x}h)\t\t\t;{self.formatted_PC}'

class OR_n(z80.instructions.OR_n):
    def __str__(self: Self) -> str:
        return f'\tor 0{self.n:02x}h\t\t;{self.formatted_PC}'

class OR_r(z80.instructions.OR_r):
    def __str__(self: Self) -> str:
        return f'\tor {self.r.lower()}\t\t\t;{self.formatted_PC}'

class OTDR(z80.instructions.OTDR):
    def __str__(self: Self) -> str:
        return f'\totdr\t\t\t;{self.formatted_PC}'

class OTIR(z80.instructions.OTIR):
    def __str__(self: Self) -> str:
        return f'\totir\t\t\t;{self.formatted_PC}'

class OUTD(z80.instructions.OUTD):
    def __str__(self: Self) -> str:
        return f'\toutd\t\t\t;{self.formatted_PC}'

class OUTI(z80.instructions.OUTI):
    def __str__(self: Self) -> str:
        return f'\touti\t\t\t;{self.formatted_PC}'

class OUT_deref_C_r(z80.instructions.OUT_deref_C_r):
    def __str__(self: Self) -> str:
        return f'\tout (c),{self.r.lower()}\t\t;{self.formatted_PC}'

class OUT_deref_n_A(z80.instructions.OUT_deref_n_A):
    def __str__(self: Self) -> str:
        return f'\tout (0{self.n:02x}h),a\t\t;{self.formatted_PC}'

class POP_IX(z80.instructions.POP_IX):
    def __str__(self: Self) -> str:
        return f'\tpop ix\t\t\t;{self.formatted_PC}'

class POP_IY(z80.instructions.POP_IY):
    def __str__(self: Self) -> str:
        return f'\tpop iy\t\t\t;{self.formatted_PC}'

class POP_qq(z80.instructions.POP_qq):
    def __str__(self: Self) -> str:
        return f'\tpop {self.qq.lower()}\t\t\t;{self.formatted_PC}'

class PUSH_IX(z80.instructions.PUSH_IX):
    def __str__(self: Self) -> str:
        return f'\tpush ix\t\t\t;{self.formatted_PC}'

class PUSH_IY(z80.instructions.PUSH_IY):
    def __str__(self: Self) -> str:
        return f'\tpush iy\t\t\t;{self.formatted_PC}'

class PUSH_qq(z80.instructions.PUSH_qq):
    def __str__(self: Self) -> str:
        return f'\tpush {self.qq.lower()}\t\t\t;{self.formatted_PC}'

class RET(z80.instructions.RET):
    def __str__(self: Self) -> str:
        return f'\tret\t\t\t;{self.formatted_PC}'

class RETI(z80.instructions.RETI):
    def __str__(self: Self) -> str:
        return f'\treti\t\t\t;{self.formatted_PC}'

class RETN(z80.instructions.RETN):
    def __str__(self: Self) -> str:
        return f'\tretn\t\t\t;{self.formatted_PC}'

class RET_cc(z80.instructions.RET_cc):
    def __str__(self: Self) -> str:
        return f'\tret {self.cc.lower()}\t\t\t;{self.formatted_PC}'

class RLA(z80.instructions.RLA):
    def __str__(self: Self) -> str:
        return f'\trla\t\t\t;{self.formatted_PC}'

class RLCA(z80.instructions.RLCA):
    def __str__(self: Self) -> str:
        return f'\trlca\t\t\t;{self.formatted_PC}'

class RLC_deref_HL(z80.instructions.RLC_deref_HL):
    def __str__(self: Self) -> str:
        return f'\trlc (hl)\t\t;{self.formatted_PC}'

class RLC_deref_IX_plus_d(z80.instructions.RLC_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\trlc (ix+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class RLC_deref_IY_plus_d(z80.instructions.RLC_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\trlc (iy+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class RLC_r(z80.instructions.RLC_r):
    def __str__(self: Self) -> str:
        return f'\trlc {self.r.lower()}\t\t;{self.formatted_PC}'

class RL_deref_HL(z80.instructions.RL_deref_HL):
    def __str__(self: Self) -> str:
        return f'\trl (hl)\t\t;{self.formatted_PC}'

class RL_deref_IX_plus_d(z80.instructions.RL_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\trl (ix+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class RL_deref_IY_plus_d(z80.instructions.RL_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\trl (iy+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class RL_r(z80.instructions.RL_r):
    def __str__(self: Self) -> str:
        return f'\trl {self.r.lower()}\t\t;{self.formatted_PC}'

class RRA(z80.instructions.RRA):
    def __str__(self: Self) -> str:
        return f'\trra\t\t\t;{self.formatted_PC}'

class RRCA(z80.instructions.RRCA):
    def __str__(self: Self) -> str:
        return f'\trrca\t\t\t;{self.formatted_PC}'

class RR_deref_HL(z80.instructions.RR_deref_HL):
    def __str__(self: Self) -> str:
        return f'\trr (hl)\t\t\t;{self.formatted_PC}'

class RR_deref_IX_plus_d(z80.instructions.RR_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\trr (ix+0{self.d:02x}h\t\t;{self.formatted_PC}'

class RR_deref_IY_plus_d(z80.instructions.RR_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\trr (iy+0{self.d:02x}h\t\t;{self.formatted_PC}'

class RR_r(z80.instructions.RR_r):
    def __str__(self: Self) -> str:
        return f'\trr {self.r.lower()}\t\t;{self.formatted_PC}'

class RST_p(z80.instructions.RST_p):
    def __str__(self: Self) -> str:
        return f'\trst {self.p:{"02x" if self.p > 10 else "x"}}{"h" if self.p > 10 else ""}\t\t\t;{self.formatted_PC}'

class SBC_deref_HL(z80.instructions.SBC_deref_HL):
    def __str__(self: Self) -> str:
        return f'\tsbc a,(hl)\t\t\t;{self.formatted_PC}'

class SBC_deref_IX_plus_d(z80.instructions.SBC_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\tsbc a,(ix+0{self.d:02x}h)\t\t\t;{self.formatted_PC}'

class SBC_deref_IY_plus_d(z80.instructions.SBC_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\tsbc a,(iy+0{self.d:02x}h)\t\t\t;{self.formatted_PC}'

class SBC_HL_ss(z80.instructions.SBC_HL_ss):
    def __str__(self: Self) -> str:
        return f'\tsbc hl,{self.ss.lower()}\t\t;{self.formatted_PC}'

class SBC_n(z80.instructions.SBC_n):
    def __str__(self: Self) -> str:
        return f'\tsbc a,0{self.n:02x}h\t\t;{self.formatted_PC}'

class SBC_r(z80.instructions.SBC_r):
    def __str__(self: Self) -> str:
        return f'\tsbc a,{self.r.lower()}\t\t\t;{self.formatted_PC}'

class SCF(z80.instructions.SCF):
    def __str__(self: Self) -> str:
        return f'\tscf\t\t\t;{self.formatted_PC}'

class SET_b_deref_HL(z80.instructions.SET_b_deref_HL):
    def __str__(self: Self) -> str:
        return f'\tset {self.b},(hl)\t\t;{self.formatted_PC}'

class SET_b_deref_IX_plus_d(z80.instructions.SET_b_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\tset {self.b},(ix+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class SET_b_deref_IY_plus_d(z80.instructions.SET_b_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\tset {self.b},(iy+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class SET_b_r(z80.instructions.SET_b_r):
    def __str__(self: Self) -> str:
        return f'\tset {self.b},{self.r.lower()}\t\t;{self.formatted_PC}'

class SLA_deref_HL(z80.instructions.SLA_deref_HL):
    def __str__(self: Self) -> str:
        return f'\tsla (hl)\t\t;{self.formatted_PC}'

class SLA_deref_IX_plus_d(z80.instructions.SLA_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\tsla (ix+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class SLA_deref_IY_plus_d(z80.instructions.SLA_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\tsla (iy+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class SLA_r(z80.instructions.SLA_r):
    def __str__(self: Self) -> str:
        return f'\tsla {self.r.lower()}\t\t;{self.formatted_PC}'

class SRL_deref_HL(z80.instructions.SRL_deref_HL):
    def __str__(self: Self) -> str:
        return f'\tsrl (hl)\t\t;{self.formatted_PC}'

class SRL_deref_IX_plus_d(z80.instructions.SRL_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\tsrl (ix+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class SRL_deref_IY_plus_d(z80.instructions.SRL_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\tsrl (iy+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class SRL_r(z80.instructions.SRL_r):
    def __str__(self: Self) -> str:
        return f'\tsrl {self.r.lower()}\t\t;{self.formatted_PC}'

class SUB_deref_HL(z80.instructions.SUB_deref_HL):
    def __str__(self: Self) -> str:
        return f'\tsub (hl)\t\t\t;{self.formatted_PC}'

class SUB_deref_IX_plus_d(z80.instructions.SUB_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\tsub (ix+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class SUB_deref_IY_plus_d(z80.instructions.SUB_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\tsub (iy+0{self.d:02x}h)\t\t;{self.formatted_PC}'

class SUB_n(z80.instructions.SUB_n):
    def __str__(self: Self) -> str:
        return f'\tsub 0{self.n:02x}h\t\t;{self.formatted_PC}'

class SUB_r(z80.instructions.SUB_r):
    def __str__(self: Self) -> str:
        return f'\tsub {self.r.lower()}\t\t\t;{self.formatted_PC}'

class XOR_deref_HL(z80.instructions.XOR_deref_HL):
    def __str__(self: Self) -> str:
        return f'\txor (hl)\t\t\t;{self.formatted_PC}'

class XOR_deref_IX_plus_d(z80.instructions.XOR_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'\txor (ix+0{self.d:02x}h)\t\t\t;{self.formatted_PC}'

class XOR_deref_IY_plus_d(z80.instructions.XOR_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'\txor (iy+0{self.d:02x}h)\t\t\t;{self.formatted_PC}'

class XOR_n(z80.instructions.XOR_n):
    def __str__(self: Self) -> str:
        return f'\txor 0{self.n:02x}h\t\t;{self.formatted_PC}'

class XOR_rprime(z80.instructions.XOR_rprime):
    def __str__(self: Self) -> str:
        return f'\txor {self.rprime.lower()}\t\t\t;{self.formatted_PC}'
