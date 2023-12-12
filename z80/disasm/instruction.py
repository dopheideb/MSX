import logging
from   typing import Self, List
import z80.instruction
import z80.instructions

class cc(z80.instruction.cc):
    def __str__(self: Self) -> str: return self.upper()
z80.instruction.FormattingType.set('cc', cc)

class d(z80.instruction.d):
    def __str__(self: Self) -> str: return f'0x{int(self):02X}'
z80.instruction.FormattingType.set('d', d)

class dd(z80.instruction.dd):
    def __str__(self: Self) -> str: return self.upper()
z80.instruction.FormattingType.set('dd', dd)

class jp(z80.instruction.dd):
    def __str__(self: Self) -> str: return f'0x{int(self):04X}'
z80.instruction.FormattingType.set('jp', jp)

class n(z80.instruction.nn):
    def __str__(self: Self) -> str: return f'0x{int(self):02X}'
z80.instruction.FormattingType.set('n', n)

class nn(z80.instruction.nn):
    def __str__(self: Self) -> str: return f'0x{int(self):04X}'
z80.instruction.FormattingType.set('nn', nn)

class PC(z80.instruction.PC):
    def __str__(self: Self) -> str: return f'{int(self):04X}'
z80.instruction.FormattingType.set('PC', PC)

class p(z80.instruction.pp):
    def __str__(self: Self) -> str: return f'0x{int(self):02X}'
z80.instruction.FormattingType.set('p', p)

class pp(z80.instruction.pp):
    def __str__(self: Self) -> str: return self.upper()
z80.instruction.FormattingType.set('pp', pp)

class qq(z80.instruction.qq):
    def __str__(self: Self) -> str: return self.upper()
z80.instruction.FormattingType.set('qq', qq)

class r(z80.instruction.pp):
    def __str__(self: Self) -> str: return self.upper()
z80.instruction.FormattingType.set('r', r)

class rr(z80.instruction.qq):
    def __str__(self: Self) -> str: return self.upper()
z80.instruction.FormattingType.set('rr', rr)

class ss(z80.instruction.qq):
    def __str__(self: Self) -> str: return self.upper()
z80.instruction.FormattingType.set('ss', ss)



class AUX:
    routines =\
    {
        ## Source: http://map.grauw.nl/resources/msxbios.php
        0x0000: "bios.CHKRAM",
        0x0008: "bios.SYNCHR",
        0x000C: "bios.RDSLT",
        0x0010: "bios.CHRGTR",
        0x0014: "bios.WRSLT",
        0x0018: "bios.OUTDO",
        0x001C: "bios.CALSLT",
        0x0020: "bios.DCOMPR",
        0x0024: "bios.ENASLT",
        0x0028: "bios.GETYPR",
        0x0030: "bios.CALLF",
        0x0038: "bios.KEYINT",
        0x003B: "bios.INITIO",
        0x003E: "bios.INIFNK",
        0x0041: "bios.DISSCR",
        0x0044: "bios.ENASCR",
        0x0047: "bios.WRTVDP(data_to_write=B, register_number=C)",
        0x004A: "bios.RDVRM(address_to_read=HL, out:A=read_value)",
        0x004D: "bios.WRTVRM(vram_address, value_to_write=A)",
        0x0050: "bios.SETRD(vram_address=HL)",
        0x0053: "bios.SETWRT(vram_address=HL)",
        0x0056: "bios.FILVRM(data_byte=A, start_address=HL, length=BC)",
        0x0059: "bios.LDIRMV",
        0x005C: "bios.LDIRVM",
        0x005F: "bios.CHGMOD",
        0x0062: "bios.CHGCLR",
        0x0066: "bios.NMI",
        0x0069: "bios.CLRSPR",
        0x006C: "bios.INITXT",
        0x006F: "bios.INIT32",
        0x0072: "bios.INIGRP",
        0x0075: "bios.INIMLT",
        0x0078: "bios.SETTXT",
        0x007B: "bios.SETT32",
        0x007E: "bios.SETGRP",
        0x0081: "bios.SETMLT",
        0x0084: "bios.CALPAT",
        0x0087: "bios.CALATR",
        0x008A: "bios.GSPSIZ",
        0x008D: "bios.GRPPRT",
        0x0090: "bios.GICINI",
        0x0093: "bios.WRTPSG(psg_register_number=A, data_to_write=E)",
        0x0096: "bios.RDPSG(psg_register_number=A)",
        0x0099: "bios.STRTMS",
        0x009C: "bios.CHSNS",
        0x009F: "bios.CHGET",
        0x00A2: "bios.CHPUT",
        0x00A5: "bios.LPTOUT",
        0x00A8: "bios.LPTSTT",
        0x00AB: "bios.CNVCHR",
        0x00AE: "bios.PINLIN",
        0x00B1: "bios.INLIN",
        0x00B4: "bios.QINLIN",
        0x00B7: "bios.BREAKX",
        0x00BA: "bios.ISCNTC",
        0x00BD: "bios.CKCNTC",
        0x00C0: "bios.BEEP",
        0x00C3: "bios.CLS",
        0x00C6: "bios.POSIT",
        0x00C9: "bios.FNKSB",
        0x00CC: "bios.ERAFNK",
        0x00CF: "bios.DSPFNK",
        0x00D2: "bios.TOTEXT",
        0x00D5: "bios.GTSTCK",
        0x00D8: "bios.GTTRIG",
        0x00DB: "bios.GTPAD",
        0x00DE: "bios.GTPDL",
        0x00E1: "bios.TAPION",
        0x00E4: "bios.TAPIN",
        0x00E7: "bios.TAPIOF",
        0x00EA: "bios.TAPOON",
        0x00ED: "bios.TAPOUT",
        0x00F0: "bios.TAPOOF",
        0x00F3: "bios.STMOTR",
        0x00F6: "bios.LFTQ",
        0x00F9: "bios.PUTQ",
        0x00FC: "bios.RIGHTC",
        0x00FF: "bios.LEFTC",
        0x0102: "bios.UPC",
        0x0105: "bios.TUPC",
        0x0108: "bios.DOWNC",
        0x010B: "bios.TDOWNC",
        0x010E: "bios.SCALXY",
        0x0111: "bios.MAPXY",
        0x0114: "bios.FETCHC",
        0x0117: "bios.STOREC",
        0x011A: "bios.SETATR",
        0x011D: "bios.READC",
        0x0120: "bios.SETC",
        0x0123: "bios.NSETCX",
        0x0126: "bios.GTASPC",
        0x0129: "bios.PNTINI",
        0x012C: "bios.SCANR",
        0x012F: "bios.SCANL",
        0x0132: "bios.CHGCAP",
        0x0135: "bios.CHGSND",
        0x0138: "bios.RSLREG",
        0x013B: "bios.WSLREG",
        0x013E: "bios.RDVDP(out:read_value=A)",
        0x0141: "bios.SNSMAT(keyboard_matrix_line=A, out:keyboard_matrix_line_value=A)",
        0x0144: "bios.PHYDIO",
        0x0147: "bios.FORMAT",
        0x014A: "bios.ISFLIO",
        0x014D: "bios.OUTDLP",
        0x0150: "bios.GETVCP",
        0x0153: "bios.GETVC2",
        0x0156: "bios.KILBUF",
        0x0159: "bios.CALBAS",
        0x015C: "bios.SUBROM",
        0x015F: "bios.EXTROM",
        0x0162: "bios.CHKSLZ",
        0x0165: "bios.CHKNEW",
        0x0168: "bios.EOL",
        0x016B: "bios.BIGFIL",
        0x016E: "bios.NSETRD",
        0x0171: "bios.NSTWRT",
        0x0174: "bios.NRDVRM",
        0x0177: "bios.NWRVRM",
        0x0180: "bios.CHGCPU",
        0x0183: "bios.GETCPU",
        0x0186: "bios.PCMPLY",
        0x0189: "bios.PCMREC",
        
        ## FIXME: Road Fighter game specific, does not belong here.
        0x4040: "4040_DE+=a",
        0x4167: "4167_increase_game_substate",
        0x45E0: "45E0_possibly___copy_to_all_three_vram_regions",
        0x4B6E: "4B6E_sound_something",
        0x72F6: "72F6_A=0xE0C0[C - 1]",
    }
    
    def add_routine(self: Self, address: int, routine_name: str) -> None:
        self.routines[address] = routine_name
    def get_routine(self: Self, address: int) -> str:
        return self.routines[address]
## Singleton
aux = AUX()



class ADC_A_deref_HL(z80.instructions.ADC_A_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} ADC A, (HL)\t\t; A += *(HL) + CY'

class ADC_A_deref_IX_plus_d(z80.instructions.ADC_A_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} ADC A, (IX+{self.d})\t\t; A += IX[{self.d}] + CY'

class ADC_A_deref_IY_plus_d(z80.instructions.ADC_A_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} ADC A, (IY+{self.d})\t\t; A += IY[{self.d}] + CY'

class ADC_A_n(z80.instructions.ADC_A_n):
    def __str__(self: Self) -> str:
        return f'{self.PC} ADC A, {self.n}\t\t; A += {self.n} + CY'

class ADC_A_r(z80.instructions.ADC_A_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} ADC A, {self.r}\t\t; A += {self.r} + CY'

class ADC_HL_ss(z80.instructions.ADC_HL_ss):
    def __str__(self: Self) -> str:
        return f'{self.PC} ADC HL, {self.ss}\t\t; HL += {self.ss} + CY'



class ADD_A_deref_HL(z80.instructions.ADD_A_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} ADD A, (HL)\t; A += *(HL)'

class ADD_A_deref_IX_plus_d(z80.instructions.ADD_A_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} ADD A, (IX+{self.d})\t; A += IX[{self.d}]'

class ADD_A_deref_IY_plus_d(z80.instructions.ADD_A_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} ADD A, (IY+{self.d})\t\t; A += IY[{self.d}]'

class ADD_A_n(z80.instructions.ADD_A_n):
    def __str__(self: Self) -> str:
        return f'{self.PC} ADD A, {self.n}\t; A += {self.n}'

class ADD_A_r(z80.instructions.ADD_A_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} ADD A, {self.r}\t\t; A += {self.r}'

class ADD_HL_ss(z80.instructions.ADD_HL_ss):
    def __str__(self: Self) -> str:
        return f'{self.PC} ADD HL, {self.ss}\t\t; HL += {self.ss}'

class ADD_IX_pp(z80.instructions.ADD_IX_pp):
    def __str__(self: Self) -> str:
        return f'{self.PC} ADD IX, {self.pp}\t\t; IX += {self.pp}'

class ADD_IY_rr(z80.instructions.ADD_IY_rr):
    def __str__(self: Self) -> str:
        return f'{self.PC} ADD IY, {self.rr}\t\t; IX += {self.rr}'



class AND_deref_HL(z80.instructions.AND_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} AND (HL)\t\t; A &= *(HL)'

class AND_deref_IX_plus_d(z80.instructions.AND_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} AND (IX+{self.d})\t; A &= IX[{self.d}]'

class AND_deref_IY_plus_d(z80.instructions.AND_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} AND (IY+{self.d})\t; A &= IY[{self.d}]'

class AND_n(z80.instructions.AND_n):
    def __str__(self: Self) -> str:
        return f'{self.PC} AND {self.n}\t\t; A &= {self._n:09_b}'

class AND_r(z80.instructions.AND_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} AND {self.r}\t\t; A &= {self.r}'



class BIT_b_deref_HL(z80.instructions.BIT_b_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} BIT {self.b}, (HL)\t; Compute *(HL) & 0x{1 << self._b:02X}, and set Z flag accordingly.'

class BIT_b_deref_IX_plus_d(z80.instructions.BIT_b_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} BIT {self.b}, (IX+{self.d})\t; Compute IX[{self.d}] & 0x{1 << self._b:02X}, and set Z flag accordingly.'

class BIT_b_deref_IY_plus_d(z80.instructions.BIT_b_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} BIT {self.b}, (IY+{self.d})\t; Compute IY[{self.d}] & 0x{1 << self._b:02X}, and set Z flag accordingly.'

class BIT_b_r(z80.instructions.BIT_b_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} BIT {self.b}, {self.r}\t\t; Compute {self.r} & 0x{1 << self._b:02X}, and set Z flag accordingly.'



class CALL_cc_nn(z80.instructions.CALL_cc_nn):
    def __str__(self: Self) -> str:
        try:
            post = f'{aux.routines[self._nn]}'
        except KeyError:
            logging.debug(f"Found unnamed call destination {self.nn}.")
            post = ''
        
        return f'{self.PC} CALL {self.cc}, {self.nn}\t; {post}'

class CALL_nn(z80.instructions.CALL_nn):
    def __str__(self: Self) -> str:
        try:
            post = f'{aux.routines[self._nn]}'
        except KeyError:
            logging.debug(f"Found unnamed call destination {self.nn}.")
            post = ''
        
        return f'{self.PC} CALL {self.nn}\t; {post}'



class CCF(z80.instructions.CCF):
    def __str__(self: Self) -> str:
        return f'{self.PC} CCF\t\t;'

class CPD(z80.instructions.CPD):
    def __str__(self: Self) -> str:
        return f'{self.PC} CPD\t\t;'

class CPDR(z80.instructions.CPDR):
    def __str__(self: Self) -> str:
        return f'{self.PC} CPDR\t\t;'

class CPI(z80.instructions.CPI):
    def __str__(self: Self) -> str:
        return f'{self.PC} CPI\t\t;'

class CPIR(z80.instructions.CPIR):
    def __str__(self: Self) -> str:
        return f'{self.PC} CPIR\t\t;'

class CPL(z80.instructions.CPL):
    def __str__(self: Self) -> str:
        return f'{self.PC} CPL\t\t;'



class CP_deref_HL(z80.instructions.CP_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} CP (HL)\t\t;'

class CP_deref_IX_plus_d(z80.instructions.CP_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} CP (IX+{self.d})\t\t;'

class CP_deref_IY_plus_d(z80.instructions.CP_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} CP (IY+{self.d})\t\t;'

class CP_n(z80.instructions.CP_n):
    def __str__(self: Self) -> str:
        return f'{self.PC} CP {self.n}\t\t;'

class CP_r(z80.instructions.CP_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} CP {self.r}\t\t;'



class DAA(z80.instructions.DAA):
    def __str__(self: Self) -> str:
        return f'{self.PC} DAA\t\t;'



class DEC_deref_HL(z80.instructions.DEC_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} DEC (HL)\t\t; --*(HL)'

class DEC_deref_IX_plus_d(z80.instructions.DEC_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} DEC (IX+{self.d})\t; --IX[{self.d}]'

class DEC_deref_IY_plus_d(z80.instructions.DEC_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} DEC (IY+{self.d})\t; --IY[{self.d}]'

class DEC_IX(z80.instructions.DEC_IX):
    def __str__(self: Self) -> str:
        return f'{self.PC} DEC IX\t\t; --IX'

class DEC_IY(z80.instructions.DEC_IY):
    def __str__(self: Self) -> str:
        return f'{self.PC} DEC IX\t\t; --IY'

class DEC_r(z80.instructions.DEC_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} DEC {self.r}\t\t; --{self.r}'

class DEC_ss(z80.instructions.DEC_ss):
    def __str__(self: Self) -> str:
        return f'{self.PC} DEC {self.ss}\t\t; --{self.ss}'

class DI(z80.instructions.DI):
    def __str__(self: Self) -> str:
        return f'{self.PC} DI\t\t\t; Disable interrupts.'

class DJNZ_e(z80.instructions.DJNZ_e):
    def __str__(self: Self) -> str:
        try:
            post = f'{aux.routines[self._jump_destination]}'
        except KeyError:
            logging.debug(f"Found unnamed jump destination {self.jump_destination}.")
            post = ''
        
        return f'{self.PC} DJNZ {self.jump_destination}\t; {post}'

class EI(z80.instructions.EI):
    def __str__(self: Self) -> str:
        return f'{self.PC} EI\t\t\t; Enable interrupts.'

class EXX(z80.instructions.EXX):
    def __str__(self: Self) -> str:
        return f'{self.PC} EXX\t\t;'

class EX_AF_AFprime(z80.instructions.EX_AF_AFprime):
    def __str__(self: Self) -> str:
        return f"{self.PC} EX AF AF'\t\t;"

class EX_deref_SP_HL(z80.instructions.EX_deref_SP_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} EX (SP), HL\t;'

class EX_deref_SP_IX(z80.instructions.EX_deref_SP_IX):
    def __str__(self: Self) -> str:
        return f'{self.PC} EX (SP), IX\t;'

class EX_deref_SP_IY(z80.instructions.EX_deref_SP_IY):
    def __str__(self: Self) -> str:
        return f'{self.PC} EX (SP), IY\t;'

class EX_DE_HL(z80.instructions.EX_DE_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} EX DE, HL\t\t;'

class HALT(z80.instructions.HALT):
    def __str__(self: Self) -> str:
        return f'{self.PC} HALT\t\t;'



class IM_0(z80.instructions.IM_0):
    def __str__(self: Self) -> str:
        return f'{self.PC} IM 0\t\t;'

class IM_1(z80.instructions.IM_1):
    def __str__(self: Self) -> str:
        return f'{self.PC} IM 1\t\t;'

class IM_2(z80.instructions.IM_2):
    def __str__(self: Self) -> str:
        return f'{self.PC} IM 2\t\t;'



class INC_deref_HL(z80.instructions.INC_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} INC (HL)\t\t; ++*(HL)'

class INC_deref_IX_plus_d(z80.instructions.INC_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} INC (IX+{self.d})\t\t; ++IX[{self.d}]'

class INC_deref_IY_plus_d(z80.instructions.INC_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} INC (IY+{self.d})\t\t; ++IY[{self.d}]'

class INC_IX(z80.instructions.INC_IX):
    def __str__(self: Self) -> str:
        return f'{self.PC} INC IX\t\t; ++IX'

class INC_IY(z80.instructions.INC_IY):
    def __str__(self: Self) -> str:
        return f'{self.PC} INC IY\t\t; ++IY'

class INC_r(z80.instructions.INC_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} INC {self.r}\t\t; ++{self.r}'

class INC_ss(z80.instructions.INC_ss):
    def __str__(self: Self) -> str:
        return f'{self.PC} INC {self.ss}\t\t; ++{self.ss}'



class IND(z80.instructions.IND):
    def __str__(self: Self) -> str:
        return f'{self.PC} IND\t\t;'

class INDR(z80.instructions.INDR):
    def __str__(self: Self) -> str:
        return f'{self.PC} INDR\t\t;'

class INI(z80.instructions.INI):
    def __str__(self: Self) -> str:
        return f'{self.PC} INI\t\t;'

class INIR(z80.instructions.INIR):
    def __str__(self: Self) -> str:
        return f'{self.PC} INIR\t\t;'



class IN_A_deref_n(z80.instructions.IN_A_deref_n):
    def __str__(self: Self) -> str:
        return f'{self.PC} IN A, ({self.n})\t\t;'

class IN_r_deref_C(z80.instructions.IN_r_deref_C):
    def __str__(self: Self) -> str:
        return f'{self.PC} IN {self.r}, (C)\t\t;'



class JP_cc_nn(z80.instructions.JP_cc_nn):
    def __str__(self: Self) -> str:
        try:
            post = f'{aux.routines[self._nn]}'
        except KeyError:
            logging.debug(f"Found unnamed jump destination {self.nn}.")
            post = ''
        
        return f'{self.PC} JP {self.cc}, {self.nn}\t; {post}'

class JP_deref_HL(z80.instructions.JP_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} JP (HL)\t\t;'

class JP_nn(z80.instructions.JP_nn):
    def __str__(self: Self) -> str:
        try:
            post = f'{aux.routines[self._nn]}'
        except KeyError:
            logging.debug(f"Found unnamed jump destination {self.nn}.")
            post = ''
        
        return f'{self.PC} JP {self.nn}\t\t; {post}'



class JR_C_e(z80.instructions.JR_C_e):
    def __str__(self: Self) -> str:
        try:
            post = f'{aux.routines[self._jump_destination]}'
        except KeyError:
            logging.debug(f"Found unnamed jump destination {self.jump_destination}.")
            post = ''
        
        return f'{self.PC} JR C, {self.jump_destination}\t; {post}'

class JR_e(z80.instructions.JR_e):
    def __str__(self: Self) -> str:
        try:
            post = f'{aux.routines[self._jump_destination]}'
        except KeyError:
            logging.debug(f"Found unnamed jump destination {self.jump_destination}.")
            post = ''
        
        return f'{self.PC} JR {self.jump_destination}\t\t; {post}'

class JR_NC_e(z80.instructions.JR_NC_e):
    def __str__(self: Self) -> str:
        try:
            post = f'{aux.routines[self._jump_destination]}'
        except KeyError:
            logging.debug(f"Found unnamed jump destination {self.jump_destination}.")
            post = ''
        
        return f'{self.PC} JR NC, {self.jump_destination}\t; {post}'

class JR_NZ_e(z80.instructions.JR_NZ_e):
    def __str__(self: Self) -> str:
        try:
            post = f'{aux.routines[self._jump_destination]}'
        except KeyError:
            logging.debug(f"Found unnamed jump destination {self.jump_destination}.")
            post = ''
        
        return f'{self.PC} JR NZ, {self.jump_destination}\t; {post}'

class JR_Z_e(z80.instructions.JR_Z_e):
    def __str__(self: Self) -> str:
        try:
            post = f'{aux.routines[self._jump_destination]}'
        except KeyError:
            logging.debug(f"Found unnamed jump destination {self.jump_destination}.")
            post = ''
        
        return f'{self.PC} JR Z, {self.jump_destination}\t; {post}'



class LDD(z80.instructions.LDD):
    def __str__(self: Self) -> str:
        return f'{self.PC} LDD\t\t;'

class LDDR(z80.instructions.LDDR):
    def __str__(self: Self) -> str:
        return f'{self.PC} LDDR\t\t;'

class LDI(z80.instructions.LDI):
    def __str__(self: Self) -> str:
        return f'{self.PC} LDI\t\t;'

class LDIR(z80.instructions.LDIR):
    def __str__(self: Self) -> str:
        return f'{self.PC} LDIR\t\t;'



class LD_A_deref_BC(z80.instructions.LD_A_deref_BC):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD A, (BC)\t\t; A = *(BC)'

class LD_A_deref_DE(z80.instructions.LD_A_deref_DE):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD A, (DE)\t\t; A = *(DE)'

class LD_A_deref_nn(z80.instructions.LD_A_deref_nn):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD A, ({self.nn})\t; A = {self.nn}'

class LD_A_I(z80.instructions.LD_A_I):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD A, I\t\t; A = I'

class LD_A_R(z80.instructions.LD_A_R):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD A, R\t\t; A = R, register A now contains a somewhat unpredictable value'



class LD_dd_deref_nn(z80.instructions.LD_dd_deref_nn):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD {self.dd}, ({self.nn})\t; {self.dd} = *({self.nn})'
    def execute(self: Self):
        self._registers.set_reg_dd(self._dd, self.nn)

class LD_dd_nn(z80.instructions.LD_dd_nn):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD {self.dd}, {self.nn}\t; {self.dd} = {self.nn}'
    def execute(self: Self):
        self._registers.set_reg_dd(self._dd, self.nn)

class LD_deref_BC_A(z80.instructions.LD_deref_BC_A):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD (BC), A\t\t; *(BC) = A'

class LD_deref_DE_A(z80.instructions.LD_deref_DE_A):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD (DE), A\t\t; *(DE) = A'

class LD_deref_HL_n(z80.instructions.LD_deref_HL_n):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD (HL), {self.n}\t; *(HL) = *(0x{self._registers.HL:02X}) = {self.n}'

class LD_deref_HL_r(z80.instructions.LD_deref_HL_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD (HL), {self.r}\t\t; *(HL) = {self.r}'

class LD_deref_IX_plus_d_n(z80.instructions.LD_deref_IX_plus_d_n):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD (IX+{self.d}), {self.n}\t; IX[{self.d}] = {self.n}'

class LD_deref_IX_plus_d_r(z80.instructions.LD_deref_IX_plus_d_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD (IX+{self.d}), {self.r}\t; IX[{self.d}] = {self.r}'

class LD_deref_IY_plus_d_n(z80.instructions.LD_deref_IY_plus_d_n):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD (IY+{self.d}), {self.n}\t; IY[{self.d}] = {self.n}'

class LD_deref_IY_plus_d_r(z80.instructions.LD_deref_IY_plus_d_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD (IY+{self.d}), {self.r}\t; IY[{self.d}] = {self.r}'

class LD_deref_nn_A(z80.instructions.LD_deref_nn_A):
    def __str__(self: Self) -> str:
        comment = ''
        if self._nn == 0xFD9A:
            comment = 'H.KEYI[0] = A, 0xC3 means "JP"'
        return f'{self.PC} LD ({self.nn}), A\t; *({self.nn}) = A' + (
            (' ' + comment) if comment else comment)

class LD_deref_nn_dd(z80.instructions.LD_deref_nn_dd):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD ({self.nn}), {self.dd}\t; *({self.nn}) = {self.dd}'

class LD_deref_nn_HL(z80.instructions.LD_deref_nn_HL):
    def __str__(self: Self) -> str:
        comment = ''
        if self.nn == 0xFD9B:
            comment = 'H.KEYI[1] = L, H.KEYI[2] = H'
        return f'{self.PC} LD ({self.nn}, HL\t;*({self.nn}) = HL (0x{self._registers.HL})' + (
            (' ' + comment) if comment else comment)
    def execute(self: Self) -> None:
        self._ram.set_word(offset=self.nn, value=self._registers.HL)

class LD_deref_nn_IX(z80.instructions.LD_deref_nn_IX):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD ({self.nn}), IX\t; *({self.nn}) = IX'

class LD_HL_deref_nn(z80.instructions.LD_HL_deref_nn):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD HL, ({self.nn})\t; HL = *({self.nn})'

class LD_IX_deref_nn(z80.instructions.LD_IX_deref_nn):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD IX, ({self.nn})\t; IX = *({self.nn})'

class LD_IX_nn(z80.instructions.LD_IX_nn):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD IX, {self.nn}\t; IX = {self.nn}'

class LD_IY_deref_nn(z80.instructions.LD_IY_deref_nn):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD IY, ({self.nn})\t; IY = *({self.nn})'

class LD_IY_nn(z80.instructions.LD_IY_nn):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD IY, {self.nn}\t; IY = {self.nn}'

class LD_I_A(z80.instructions.LD_I_A):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD I, A\t\t; I = A'

class LD_R_A(z80.instructions.LD_R_A):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD R, A\t\t; Weird!!!'

class LD_r_deref_HL(z80.instructions.LD_r_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD {self.r}, (HL)\t\t; {self.r} = *(HL)'

class LD_r_deref_IX_plus_d(z80.instructions.LD_r_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD {self.r}, (IX+{self.d})\t; {self.r} = IX[{self.d}]'

class LD_r_deref_IY_plus_d(z80.instructions.LD_r_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD {self.r}, (IY+{self.d})\t; {self.r} = IY[{self.d}]'

class LD_r_n(z80.instructions.LD_r_n):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD {self.r}, {self.n}\t\t; {self.r} = {self.n}'
    def execute(self: Self):
        self._registers.set_r_n(self._r, self.n)

class LD_r_rprime(z80.instructions.LD_r_rprime):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD {self.r}, {self.rprime}\t\t; {self.r} = {self.rprime}'

class LD_SP_HL(z80.instructions.LD_SP_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD SP, HL\t\t; SP = HL'

class LD_SP_IX(z80.instructions.LD_SP_IX):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD SP, IX\t\t; SP = IX'

class LD_SP_IY(z80.instructions.LD_SP_IY):
    def __str__(self: Self) -> str:
        return f'{self.PC} LD SP, IY\t\t; SP = IY'

class NEG(z80.instructions.NEG):
    def __str__(self: Self) -> str:
        return f'{self.PC} NEG\t\t;'

class NOP(z80.instructions.NOP):
    def __str__(self: Self) -> str:
        return f'{self.PC} NOP\t\t;'

class OR_deref_HL(z80.instructions.OR_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} OR (HL)\t\t; A |= *(HL)'

class OR_deref_IX_plus_d(z80.instructions.OR_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} OR (IX+{self.d})\t\t; A |= IX[{self.d}]'

class OR_deref_IY_plus_d(z80.instructions.OR_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} OR (IY+{self.d})\t\t; A |= IY[{self.d}]'

class OR_n(z80.instructions.OR_n):
    def __str__(self: Self) -> str:
        return f'{self.PC} OR {self.n}\t\t; A |= {self.n}'

class OR_r(z80.instructions.OR_r):
    def __str__(self: Self) -> str:
        if self._r == 0b111:
            return f'{self.PC} OR {self.r}\t\t; A |= {self.r}, set flag Z/NZ.'
        return f'{self.PC} OR {self.r}\t\t; A |= {self.r}'

class OTDR(z80.instructions.OTDR):
    def __str__(self: Self) -> str:
        return f'{self.PC} OTDR\t\t\t;'

class OTIR(z80.instructions.OTIR):
    def __str__(self: Self) -> str:
        return f'{self.PC} OTIR\t\t\t;'

class OUTD(z80.instructions.OUTD):
    def __str__(self: Self) -> str:
        return f'{self.PC} OUTD\t\t\t;'

class OUTI(z80.instructions.OUTI):
    def __str__(self: Self) -> str:
        return f'{self.PC} OUTI\t\t\t;'

class OUT_deref_C_r(z80.instructions.OUT_deref_C_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} OUT (C), {self.r}\t\t;'

class OUT_deref_n_A(z80.instructions.OUT_deref_n_A):
    def __str__(self: Self) -> str:
        return f'{self.PC} OUT ({self.n}), A\t\t;'

class POP_IX(z80.instructions.POP_IX):
    def __str__(self: Self) -> str:
        return f'{self.PC} POP IX\t\t;'

class POP_IY(z80.instructions.POP_IY):
    def __str__(self: Self) -> str:
        return f'{self.PC} POP IY\t\t;'

class POP_qq(z80.instructions.POP_qq):
    def __str__(self: Self) -> str:
        return f'{self.PC} POP {self.qq}\t\t;'

class PUSH_IX(z80.instructions.PUSH_IX):
    def __str__(self: Self) -> str:
        return f'{self.PC} PUSH IX\t\t;'

class PUSH_IY(z80.instructions.PUSH_IY):
    def __str__(self: Self) -> str:
        return f'{self.PC} PUSH IY\t\t;'

class PUSH_qq(z80.instructions.PUSH_qq):
    def __str__(self: Self) -> str:
        return f'{self.PC} PUSH {self.qq}\t\t;'

class RET(z80.instructions.RET):
    def __str__(self: Self) -> str:
        return f'{self.PC} RET\t\t;'

class RETI(z80.instructions.RETI):
    def __str__(self: Self) -> str:
        return f'{self.PC} RETI\t\t;'

class RETN(z80.instructions.RETN):
    def __str__(self: Self) -> str:
        return f'{self.PC} RETN\t\t;'

class RET_cc(z80.instructions.RET_cc):
    def __str__(self: Self) -> str:
        return f'{self.PC} RET {self.cc}\t\t;if ({self.cc}) return'

class RLA(z80.instructions.RLA):
    def __str__(self: Self) -> str:
        return f'{self.PC} RLA\t\t;'

class RLCA(z80.instructions.RLCA):
    def __str__(self: Self) -> str:
        return f'{self.PC} RLCA\t\t;'

class RLC_deref_HL(z80.instructions.RLC_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} RLC (HL)\t\t;'

class RLC_deref_IX_plus_d(z80.instructions.RLC_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} RLC (IX+{self.d})\t\t;'

class RLC_r(z80.instructions.RLC_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} RLC {self.r}\t\t;'

class RL_deref_HL(z80.instructions.RL_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} RLC (HL)\t\t;'

class RL_deref_IX_plus_d(z80.instructions.RL_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} RL (IX+{self.d})\t\t;'

class RL_deref_IY_plus_d(z80.instructions.RL_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} RL (IY+{self.d})\t\t;'

class RL_r(z80.instructions.RL_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} RL {self.r}\t\t;'

class RRA(z80.instructions.RRA):
    def __str__(self: Self) -> str:
        return f'{self.PC} RRA\t\t;'

class RRCA(z80.instructions.RRCA):
    def __str__(self: Self) -> str:
        return f'{self.PC} RRCA\t\t;'

class RR_deref_HL(z80.instructions.RR_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} RR (HL)\t\t;'

class RR_deref_IX_plus_d(z80.instructions.RR_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} RR (IX+{self.d})\t\t;'

class RR_deref_IY_plus_d(z80.instructions.RR_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} RR (IY+{self.d})\t\t;'

class RR_r(z80.instructions.RR_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} RR {self.r}\t\t;'

class RST_p(z80.instructions.RST_p):
    def __str__(self: Self) -> str:
        return f'{self.PC} RST {self.p}\t\t;'

class SBC_HL_ss(z80.instructions.SBC_HL_ss):
    def __str__(self: Self) -> str:
        return f'{self.PC} SBC HL, {self.ss}\t\t;'

class SCF(z80.instructions.SCF):
    def __str__(self: Self) -> str:
        return f'{self.PC} SCF\t\t;'

class SET_b_deref_HL(z80.instructions.SET_b_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} SET {self.b}, (HL)\t\t;'

class SET_b_deref_IX_plus_d(z80.instructions.SET_b_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} SET {self.b}, (IX+{self.d})\t\t;'

class SET_b_deref_IY_plus_d(z80.instructions.SET_b_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} SET {self.b}, (IY+{self.d})\t\t;'

class SET_b_r(z80.instructions.SET_b_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} SET {self.b}, {self.r}\t\t;'

class SLA_deref_HL(z80.instructions.SLA_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} SLA (HL)\t\t;'

class SLA_deref_IX_plus_d(z80.instructions.SLA_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} SLA (IX+{self.d})\t\t;'

class SLA_deref_IY_plus_d(z80.instructions.SLA_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} SLA (IY+{self.d})\t\t;'

class SLA_r(z80.instructions.SLA_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} SLA {self.r})\t\t;'

class SRL_deref_HL(z80.instructions.SRL_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} SRL (HL)\t\t;'

class SRL_deref_IX_plus_d(z80.instructions.SRL_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} SRL (IX+{self.d})\t\t;'

class SRL_deref_IY_plus_d(z80.instructions.SRL_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} SRL (IY+{self.d})\t\t;'

class SRL_r(z80.instructions.SRL_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} SRL {self.r}\t\t;'

class SUB_deref_HL(z80.instructions.SUB_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} SUB (HL)\t\t; A -= *(HL)'

class SUB_deref_IX_plus_d(z80.instructions.SUB_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} SUB (IX+{self.d})\t\t; A -= IX[{self.d}]'

class SUB_deref_IY_plus_d(z80.instructions.SUB_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} SUB (IY+{self.d})\t\t; A -= IY[{self.d}]'

class SUB_n(z80.instructions.SUB_n):
    def __str__(self: Self) -> str:
        return f'{self.PC} SUB {self.n}\t\t; A -= {self.n}'

class SUB_r(z80.instructions.SUB_r):
    def __str__(self: Self) -> str:
        return f'{self.PC} SUB {self.r}\t\t; A -= {self.r}'

class XOR_deref_HL(z80.instructions.XOR_deref_HL):
    def __str__(self: Self) -> str:
        return f'{self.PC} XOR (HL)\t\t; A ^= *(HL)'

class XOR_deref_IX_plus_d(z80.instructions.XOR_deref_IX_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} XOR (IX+{self.d})\t\t; A ^= IX[{self.d}]'

class XOR_deref_IY_plus_d(z80.instructions.XOR_deref_IY_plus_d):
    def __str__(self: Self) -> str:
        return f'{self.PC} XOR (IY+{self.d})\t\t; A ^= IY[{self.d}]'

class XOR_n(z80.instructions.XOR_n):
    def __str__(self: Self) -> str:
        return f'{self.PC} XOR {self.n}\t\t; A ^= {self.n}'

class XOR_rprime(z80.instructions.XOR_rprime):
    def __str__(self: Self) -> str:
        if self.rprime == 0b111:
            return f'{self.PC} XOR {self.rprime}\t\t; A = 0, set flags.'
        return f'{self.PC} XOR {self.rprime}\t\t; A ^= {self.rprime}'
