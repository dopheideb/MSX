import logging
from   typing import Self, List
import z80.instruction
import z80.instructions

class AUX:
    routines =\
    {
        ## Source: http://map.grauw.nl/resources/msxbios.php
        0x0000: "CHKRAM",
        0x0008: "SYNCHR",
        0x000C: "RDSLT",
        0x0010: "CHRGTR",
        0x0014: "WRSLT",
        0x0018: "OUTDO",
        0x001C: "CALSLT",
        0x0020: "DCOMPR",
        0x0024: "ENASLT",
        0x0028: "GETYPR",
        0x0030: "CALLF",
        0x0038: "KEYINT",
        0x003B: "INITIO",
        0x003E: "INIFNK",
        0x0041: "DISSCR",
        0x0044: "ENASCR",
        0x0047: "WRTVDP(data_to_write=B, register_number=C)",
        0x004A: "RDVRM",
        0x004D: "WRTVRM",
        0x0050: "SETRD",
        0x0053: "SETWRT",
        0x0056: "FILVRM",
        0x0059: "LDIRMV",
        0x005C: "LDIRVM",
        0x005F: "CHGMOD",
        0x0062: "CHGCLR",
        0x0066: "NMI",
        0x0069: "CLRSPR",
        0x006C: "INITXT",
        0x006F: "INIT32",
        0x0072: "INIGRP",
        0x0075: "INIMLT",
        0x0078: "SETTXT",
        0x007B: "SETT32",
        0x007E: "SETGRP",
        0x0081: "SETMLT",
        0x0084: "CALPAT",
        0x0087: "CALATR",
        0x008A: "GSPSIZ",
        0x008D: "GRPPRT",
        0x0090: "GICINI",
        0x0093: "WRTPSG(psg_register_number=A, data_to_write=E)",
        0x0096: "RDPSG(psg_register_number=A)",
        0x0099: "STRTMS",
        0x009C: "CHSNS",
        0x009F: "CHGET",
        0x00A2: "CHPUT",
        0x00A5: "LPTOUT",
        0x00A8: "LPTSTT",
        0x00AB: "CNVCHR",
        0x00AE: "PINLIN",
        0x00B1: "INLIN",
        0x00B4: "QINLIN",
        0x00B7: "BREAKX",
        0x00BA: "ISCNTC",
        0x00BD: "CKCNTC",
        0x00C0: "BEEP",
        0x00C3: "CLS",
        0x00C6: "POSIT",
        0x00C9: "FNKSB",
        0x00CC: "ERAFNK",
        0x00CF: "DSPFNK",
        0x00D2: "TOTEXT",
        0x00D5: "GTSTCK",
        0x00D8: "GTTRIG",
        0x00DB: "GTPAD",
        0x00DE: "GTPDL",
        0x00E1: "TAPION",
        0x00E4: "TAPIN",
        0x00E7: "TAPIOF",
        0x00EA: "TAPOON",
        0x00ED: "TAPOUT",
        0x00F0: "TAPOOF",
        0x00F3: "STMOTR",
        0x00F6: "LFTQ",
        0x00F9: "PUTQ",
        0x00FC: "RIGHTC",
        0x00FF: "LEFTC",
        0x0102: "UPC",
        0x0105: "TUPC",
        0x0108: "DOWNC",
        0x010B: "TDOWNC",
        0x010E: "SCALXY",
        0x0111: "MAPXY",
        0x0114: "FETCHC",
        0x0117: "STOREC",
        0x011A: "SETATR",
        0x011D: "READC",
        0x0120: "SETC",
        0x0123: "NSETCX",
        0x0126: "GTASPC",
        0x0129: "PNTINI",
        0x012C: "SCANR",
        0x012F: "SCANL",
        0x0132: "CHGCAP",
        0x0135: "CHGSND",
        0x0138: "RSLREG",
        0x013B: "WSLREG",
        0x013E: "RDVDP",
        0x0141: "SNSMAT(keyboard_matrix_line=A)",
        0x0144: "PHYDIO",
        0x0147: "FORMAT",
        0x014A: "ISFLIO",
        0x014D: "OUTDLP",
        0x0150: "GETVCP",
        0x0153: "GETVC2",
        0x0156: "KILBUF",
        0x0159: "CALBAS",
        0x015C: "SUBROM",
        0x015F: "EXTROM",
        0x0162: "CHKSLZ",
        0x0165: "CHKNEW",
        0x0168: "EOL",
        0x016B: "BIGFIL",
        0x016E: "NSETRD",
        0x0171: "NSTWRT",
        0x0174: "NRDVRM",
        0x0177: "NWRVRM",
        0x0180: "CHGCPU",
        0x0183: "GETCPU",
        0x0186: "PCMPLY",
        0x0189: "PCMREC",
    }
    
    def add_routine(self: Self, address: int, routine_name: str) -> None:
        self.routines[address] = routine_name
    def get_routine(self: Self, address: int) -> str:
        return self.routines[address]
## Singleton
aux = AUX()

z80.instruction.Instruction.set_PC_formatter(func=lambda instr: f'{instr.PC:04X}')



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
        return f'{self.formatted_PC} ADD HL {self.ss}\t\t; HL += {self.ss}'

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
        return f'{self.formatted_PC} AND 0x{self.n:02X}\t; A &= {self.n:09_b}'

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
            post = f'{aux.routines[self.nn]}'
        except KeyError:
            post = ''
        
        return f'{self.formatted_PC} CALL 0x{self.nn:04X}\t; {post}'

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
        return f'{self.formatted_PC} DEC {self.r}\t\t; --{self.r}'

class DEC_ss(z80.instructions.DEC_ss):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class DI(z80.instructions.DI):
    def __str__(self: Self) -> str:
        return f'{self.formatted_PC} {self.name()}\t; Disable interrupts.'

class DJNZ_e(z80.instructions.DJNZ_e):
    def __str__(self: Self) -> str:
        return f'{self.formatted_PC} DJNZ 0x{self.jump_destination:04X}\t;'

class EI(z80.instructions.EI):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class EXX(z80.instructions.EXX):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class EX_AF_AFprime(z80.instructions.EX_AF_AFprime):
    def __str__(self: Self) -> str:
        return f"{self.formatted_PC} EX AF AF'\t\t;"

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
        return f'{self.formatted_PC} EX DE, HL\t\t;'

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
        return f'{self.formatted_PC} INC {self.r}\t\t; ++{self.r}'

class INC_ss(z80.instructions.INC_ss):
    def __str__(self: Self) -> str:
        return f'{self.formatted_PC} INC {self.ss}\t\t; ++{self.ss}'

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
        return f'{self.formatted_PC} JP 0x{self.nn:04X}'

class JR_C_e(z80.instructions.JR_C_e):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class JR_e(z80.instructions.JR_e):
    def __str__(self: Self) -> str:
        return f'{self.formatted_PC} JR 0x{self.jump_destination:04X}\t;'

class JR_NC_e(z80.instructions.JR_NC_e):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class JR_NZ_e(z80.instructions.JR_NZ_e):
    def __str__(self: Self) -> str:
        return f'{self.formatted_PC} JR NZ 0x{self.jump_destination:04X}\t;'

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
        return f'{self.formatted_PC} LDIR\t\t;'

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
        return f'{self.formatted_PC} LD {self.dd}, (0x{self.nn:04X})\t; {self.dd} = *(0x{self.nn:04X})'
    def execute(self: Self):
        self._registers.set_reg_dd(self._dd, self.nn)

class LD_dd_nn(z80.instructions.LD_dd_nn):
    def __str__(self: Self) -> str:
        return f'{self.formatted_PC} LD {self.dd}, 0x{self.nn:04X}\t; {self.dd} = 0x{self.nn:04X}'
    def execute(self: Self):
        self._registers.set_reg_dd(self._dd, self.nn)

class LD_deref_BC_A(z80.instructions.LD_deref_BC_A):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_deref_DE_A(z80.instructions.LD_deref_DE_A):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_deref_HL_n(z80.instructions.LD_deref_HL_n):
    def __str__(self: Self) -> str:
        return f'{self.formatted_PC} LD (HL), 0x{self.n:02X}\t; *(HL) = *(0x{self._registers.HL:04X}) = 0x{self.n:02X}'

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
        return f'{self.formatted_PC} *(0x{self.nn:04X}) := A (0x{self._registers.A:02X})' + (
            (' ' + comment) if comment else comment)

class LD_deref_nn_dd(z80.instructions.LD_deref_nn_dd):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_deref_nn_HL(z80.instructions.LD_deref_nn_HL):
    def __str__(self: Self) -> str:
        comment = ''
        if self.nn == 0xFD9B:
            comment = 'H.KEYI[1] = L, H.KEYI[2] = H'
        return f'{self.formatted_PC} *(0x{self.nn:04X}) := HL (0x{self._registers.HL:04X})' + (
            (' ' + comment) if comment else comment)
    def execute(self: Self) -> None:
        #self._ram[self.nn+0] = self._registers.L
        #self._ram[self.nn+1] = self._registers.H
        self._ram.set_word(offset=self.nn, value=self._registers.HL)

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
        return f'{self.formatted_PC} LD {self.r}, (HL)\t\t;'

class LD_r_deref_IX_plus_d(z80.instructions.LD_r_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_r_deref_IY_plus_d(z80.instructions.LD_r_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class LD_r_n(z80.instructions.LD_r_n):
    def __str__(self: Self) -> str:
        return f'{self.formatted_PC} LD {self.r}, 0x{self.n:02X}\t\t; {self.r} = 0x{self.n:02X}'
    def execute(self: Self):
        self._registers.set_r_n(self._r, self.n)

class LD_r_rprime(z80.instructions.LD_r_rprime):
    def __str__(self: Self) -> str:
        return f'{self.formatted_PC} LD {self.r}, {self.rprime}\t\t; {self.r} = {self.rprime}'

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
        return f'{self.formatted_PC} POP {self.qq}\t\t;'

class PUSH_IX(z80.instructions.PUSH_IX):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class PUSH_IY(z80.instructions.PUSH_IY):
    def __str__(self: Self) -> str:
        return "STUB " + super().__str__()

class PUSH_qq(z80.instructions.PUSH_qq):
    def __str__(self: Self) -> str:
        return f'{self.formatted_PC} PUSH {self.qq}\t\t;'

class RET(z80.instructions.RET):
    def __str__(self: Self) -> str:
        return f'{self.formatted_PC} RET\t\t;'

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
        return f'{self.formatted_PC} SUB {self.r}\t\t; A -= {self.r}'

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
        return f'{self.formatted_PC} A ^= {self.n:02X}'

class XOR_rprime(z80.instructions.XOR_rprime):
    def __str__(self: Self) -> str:
        if self.rprime == 0b111:
            return f'{self.formatted_PC} A = 0, set flags.'
        return f'{self.formatted_PC} A ^= {self.rprime}'
