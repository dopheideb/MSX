import abc
import collections
import logging
import re
import sys
from   typing import Self, Dict, List, Type
import z80.ram
import z80.registers



class b(int):
    def __str__(self: Self) -> str: return f'{int(self)}'
class d(int):
    def __str__(self: Self) -> str: return f'0{int(self):02x}h'
class cc(str):
    def __str__(self: Self) -> str: return self.lower()
class dd(str):
    def __str__(self: Self) -> str: return self.lower()
class e(int):
    def __str__(self: Self) -> str: return f'{2+int(self):+}'
class jp(int):
    def __str__(self: Self) -> str: return f'0{int(self):04x}h'
class PC(int):
    def __str__(self: Self) -> str: return f'{int(self):04x}'
class p(int):
    def __str__(self: Self) -> str: return f'{int(self):{"02x" if self >= 10 else ""}}{"h" if self >= 10 else ""}'
class n(int):
    def __str__(self: Self) -> str: return f'0{int(self):02x}h'
class nn(int):
    def __str__(self: Self) -> str: return f'0{int(self):04x}h'
class pp(str):
    def __str__(self: Self) -> str: return self.lower()
class qq(str):
    def __str__(self: Self) -> str: return self.lower()
class r(str):
    def __str__(self: Self) -> str: return self.lower()
class rr(str):
    def __str__(self: Self) -> str: return self.lower()
class ss(str):
    def __str__(self: Self) -> str: return self.lower()

class FormattingType:
    b  = b
    cc = cc
    d  = d
    dd = dd
    e  = e
    jp = jp
    n  = n
    nn = nn
    PC = PC
    p  = p
    pp = pp
    qq = qq
    r  = r
    rr = rr
    ss = ss
    @classmethod
    def set(cls, typename, formatting_type):
        match typename:
            case 'b' : cls.b  = formatting_type
            case 'cc': cls.cc = formatting_type
            case 'd' : cls.d  = formatting_type
            case 'dd': cls.dd = formatting_type
            case 'e' : cls.e  = formatting_type
            case 'jp': cls.jp = formatting_type
            case 'n' : cls.n  = formatting_type
            case 'nn': cls.nn = formatting_type
            case 'PC': cls.PC = formatting_type
            case 'p' : cls.p  = formatting_type
            case 'pp': cls.pp = formatting_type
            case 'qq': cls.qq = formatting_type
            case 'r' : cls.r  = formatting_type
            case 'rr': cls.rr = formatting_type
            case 'ss': cls.ss = formatting_type
            case _:
                raise ValueError(f"Unknown typename '{typename}'.")

class Instruction(abc.ABC):
    ## The Z80 has instruction classes in which the instruction can be used on a 
    ## fixed set of register pairs.
    ## 
    ## Example for cc: JP cc, nn
    cc2name =\
    {
        0b000: 'NZ',	## 0
        0b001: 'Z',	## 1
        0b010: 'NC',	## 2
        0b011: 'C',	## 3
        0b100: 'PO',	## 4
        0b101: 'PE',	## 5
        0b110: 'P',	## 6
        0b111: 'M',	## 7
    }
    
    
    
    ## The Z80 has instruction classes in which the instruction can be used on a 
    ## fixed set of register pairs.
    ## 
    ## Example for dd: LD dd, nn
    dd2name =\
    {
        0b00: 'BC',	## 0
        0b01: 'DE',	## 1
        0b10: 'HL',	## 2
        0b11: 'SP',	## 3
    }
    
    
    
    ## The Z80 has instruction classes in which the instruction can be used on a 
    ## fixed set of register pairs.
    ## 
    ## Example for pp: ADD IX, pp
    ## 
    ## FIXME: Page 194 calls it wrongfully ss.
    pp2name =\
    {
        0b00: 'BC',	## 0
        0b01: 'DE',	## 1
        0b10: 'IX',	## 2
        0b11: 'SP',	## 3
    }
    
    
    
    ## The Z80 has instruction classes in which the instruction can be used on a 
    ## fixed set of register pairs.
    ## 
    ## Example for qq: PUSH qq
    qq2name =\
    {
        0b00: 'BC',	## 0
        0b01: 'DE',	## 1
        0b10: 'HL',	## 2
        0b11: 'AF',	## 3
    }
    
    
    
    ## The Z80 has instruction classes in which the instruction can be used on a 
    ## fixed set of registers.
    ## 
    ## Example for r: LD r, n
    r2name =\
    {
        0b000: 'B',	## 0
        0b001: 'C',	## 1
        0b010: 'D',	## 2
        0b011: 'E',	## 3
        0b100: 'H',	## 4
        0b101: 'L',	## 5
			## 6
        0b111: 'A',	## 7
    }
    
    
    
    ## The Z80 has instruction classes in which the instruction can be used on a 
    ## fixed set of register pairs.
    ## 
    ## Example for rr: ADD IY, rr
    ## 
    ## FIXME: Page 196 calls it wrongfully ss.
    rr2name =\
    {
        0b00: 'BC',	## 0
        0b01: 'DE',	## 1
        0b10: 'IY',	## 2
        0b11: 'SP',	## 3
    }
    
    
    
    ## The Z80 has instruction classes in which the instruction can be used on a 
    ## fixed set of register pairs.
    ## 
    ## Example for ss: INC ss
    ## 
    ## Note: exactly the same as dd...
    ss2name =\
    {
        0b00: 'BC',	## 0
        0b01: 'DE',	## 1
        0b10: 'HL',	## 2
        0b11: 'SP',	## 3
    }
    
    
    
    t2p =\
    {
        0b000: 0x00,
        0b001: 0x08,
        0b010: 0x10,
        0b011: 0x18,
        0b100: 0x20,
        0b101: 0x28,
        0b110: 0x30,
        0b111: 0x38,
    }
    
    
    
    instruction_sets: Dict[str, List['Instruction']] = collections.defaultdict(list)
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.instruction_sets[cls.__module__].append(cls)
    
    def __init__(self: Self,
        registers: z80.registers.Registers,
        ram: z80.ram.RAM,
        opcode: int,
    ) -> None:
        self._registers = registers
        self._ram = ram
        self._opcode = opcode
        ## The program counter will change, and soon. We make a copy of the 
        ## current value so we can inspect the program counter without having 
        ## to hurry.
        self._PC = PC(self._registers.PC)
    
    @property
    def opcode(self: Self) -> int: return self._opcode
    
    @classmethod
    @abc.abstractmethod
    def opcodes(cls) -> List[int]: pass
    
    @property
    @abc.abstractmethod
    def size(self: Self) -> int: pass
    
    @property
    def PC(self: Self) -> int:
        return FormattingType.PC(self._PC)

class Illegal(Instruction):
    @classmethod
    def opcodes(cls) -> List[int]:
        return []
    
    @property
    def size(self: Self) -> int:
        if self._opcode <= 0xff:
            return 1
        if self._opcode <= 0xffff:
            return 2
        if self._opcode <= 0xffffff:
            return 3
        return 4
    
    def __str__(self: Self) -> str:
        return f'Illegal (or unknown) opcode 0x{self._opcode:02X}.'



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    
    b = range(8)
    cc = range(8)
    dd = range(4)
    pp = range(4)
    qq = range(4)
    rr = range(4)
    r = [ x for x in range(8) if x != 0b110 ]
    ss = range(4)
    t = range(8)
    
    ## Instruction are in the same order as "Z80 CPU User Manual" (um0080.pdf)
    instructions =\
    {
        ######################
        ##                  ##
        ## 8-Bit Load Group ##
        ##                  ##
        ######################
        ## Page 71
        "LD r, r'":\
        {
            'opcodes': [ (0b01_000_000 | (i << 3) | (j << 0) ) for i in r for j in r ],
            'size': 1,
            'operands': [ 'r3', 'rprime0' ],
        },
        
        ## Page 72
        "LD r, n":\
        {
            'opcodes': [ (0b00_000_110 | (i << 3)) for i in r ],
            'size': 2,
            'operands': [ 'r3', 'n' ],
        },
        
        ## Page 74
        "LD r, (HL)":\
        {
            'opcodes': [ (0b01_000_110 | (i << 3)) for i in r ],
            'size': 1,
            'operands': [ 'r3' ],
        },
        
        ## Page 75
        "LD r, (IX+d)":\
        {
            'opcodes': [ (0xDD00 | 0b01_000_110 | (i << 3)) for i in r ],
            'size': 3,
            'operands': [ 'r3', 'd' ],
        },
        
        ## Page 77
        "LD r, (IY+d)":\
        {
            'opcodes': [ (0xFD00 | 0b01_000_110 | (i << 3)) for i in r ],
            'size': 3,
            'operands': [ 'r3', 'd' ],
        },
        
        ## Page 79
        "LD (HL), r":\
        {
            'opcodes': [ (0b01110_000 | (i << 0)) for i in r ],
            'size': 1,
            'operands': [ 'r0' ],
        },
        
        ## Page 81
        "LD (IX+d), r":\
        {
            'opcodes': [ (0xDD00 | 0b01110_000 | (i << 0)) for i in r ],
            'size': 3,
            'operands': [ 'd', 'r0' ],
        },
        
        ## Page 83
        "LD (IY+d), r":\
        {
            'opcodes': [ (0xFD00 | 0b01110_000 | (i << 0)) for i in r ],
            'size': 3,
            'operands': [ 'd', 'r0' ],
        },
        
        ## Page 85
        "LD (HL), n":\
        {
            'opcodes': [ 0x36 ],
            'size': 2,
            'operands': [ 'n' ],
        },
        
        ## Page 86
        "LD (IX+d), n":\
        {
            'opcodes': [ 0xDD36 ],
            'size': 4,
            'operands': [ 'd', 'n' ],
        },
        
        ## Page 87
        "LD (IY+d), n":\
        {
            'opcodes': [ 0xFD36 ],
            'size': 4,
            'operands': [ 'd', 'n' ],
        },
        
        ## Page 88
        "LD A, (BC)":\
        {
            'opcodes': [ 0x0A ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 89
        "LD A, (DE)":\
        {
            'opcodes': [ 0x1A ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 90
        "LD A, (nn)":\
        {
            'opcodes': [ 0x3A ],
            'size': 3,
            'operands': [ 'nn' ],
        },
        
        ## Page 91
        "LD (BC), A":\
        {
            'opcodes': [ 0x02 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 92
        "LD (DE), A":\
        {
            'opcodes': [ 0x12 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 93
        "LD (nn), A":\
        {
            'opcodes': [ 0x32 ],
            'size': 3,
            #'operands': [ 'nn', 'A' ],
            'operands': [ 'nn' ],
        },
        
        ## Page 94
        "LD A, I":\
        {
            'opcodes': [ 0xED57 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 95
        "LD A, R":\
        {
            'opcodes': [ 0xED5F ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 96
        "LD I, A":\
        {
            'opcodes': [ 0xED47 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 97
        "LD R, A":\
        {
            'opcodes': [ 0xED4F ],
            'size': 2,
            'operands': [],
        },
        
        
        
        #######################
        ##                   ##
        ## 16-Bit Load Group ##
        ##                   ##
        #######################
        ## Page 99
        "LD dd, nn":\
        {
            'opcodes': [ (0b00_00_0001 | (i << 4)) for i in dd ],
            'size': 3,
            'operands': [ 'dd4', 'nn' ],
        },
        
        ## Page 100
        "LD IX, nn":\
        {
            'opcodes': [ 0xDD21 ],
            'size': 4,
            'operands': [ 'nn' ],
        },
        
        ## Page 101
        "LD IY, nn":\
        {
            'opcodes': [ 0xFD21 ],
            'size': 4,
            'operands': [ 'nn' ],
        },
        
        ## Page 102
        "LD HL, (nn)":\
        {
            'opcodes': [ 0x2A ],
            'size': 3,
            'operands': [ 'nn' ],
        },
        
        ## Page 103
        "LD dd, (nn)":\
        {
            'opcodes': [ (0xED00 | 0b01_00_1011 | (i << 4)) for i in dd ],
            'size': 4,
            'operands': [ 'dd4', 'nn' ],
        },
        
        ## Page 105
        "LD IX, (nn)":\
        {
            'opcodes': [ 0xDD2A ],
            'size': 4,
            'operands': [ 'nn' ],
        },
        
        ## Page 106
        "LD IY, (nn)":\
        {
            'opcodes': [ 0xFD2A ],
            'size': 4,
            'operands': [ 'nn' ],
        },
        
        ## Page 107
        "LD (nn), HL":\
        {
            'opcodes': [ 0x22 ],
            'size': 3,
            'operands': [ 'nn' ],
        },
        
        ## Page 108
        "LD (nn), dd":\
        {
            'opcodes': [ (0xED00 | 0b01_00_0011 | (i << 4)) for i in dd ],
            'size': 4,
            'operands': [ 'nn', 'dd4' ],
        },
        
        ## Page 110
        "LD (nn), IX":\
        {
            'opcodes': [ 0xDD22 ],
            'size': 4,
            'operands': [ 'nn' ],
        },
        
        ## Page 111
        "LD (nn), IX":\
        {
            'opcodes': [ 0xFD22 ],
            'size': 4,
            'operands': [ 'nn' ],
        },
        
        ## Page 112
        "LD SP, HL":\
        {
            'opcodes': [ 0xF9 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 113
        "LD SP, IX":\
        {
            'opcodes': [ 0xDDF9 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 114
        "LD SP, IY":\
        {
            'opcodes': [ 0xFDF9 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 115
        "PUSH qq":\
        {
            'opcodes': [ (0b11_00_0101 | (i << 4)) for i in qq ],
            'size': 1,
            'operands': [ 'qq4' ],
        },
        
        ## Page 117
        "PUSH IX":\
        {
            'opcodes': [ 0xDDE5 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 118
        "PUSH IY":\
        {
            'opcodes': [ 0xFDE5 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 119
        "POP qq":\
        {
            'opcodes': [ (0b11_00_0001 | (i << 4)) for i in qq ],
            'size': 1,
            'operands': [ 'qq4' ],
        },
        
        ## Page 121
        "POP IX":\
        {
            'opcodes': [ 0xDDE1 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 121
        "POP IY":\
        {
            'opcodes': [ 0xFDE1 ],
            'size': 2,
            'operands': [],
        },
        
        
        
        ################################################
        ##                                            ##
        ## Exchange, Block Transfer, and Search Group ##
        ##                                            ##
        ################################################
        ## Page 124
        "EX DE, HL":\
        {
            'opcodes': [ 0xEB ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 125
        "EX AF, AF'":\
        {
            'opcodes': [ 0x08 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 126
        "EXX":\
        {
            'opcodes': [ 0xD9 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 127
        "EX (SP), HL":\
        {
            'opcodes': [ 0xE3 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 128
        "EX (SP), IX":\
        {
            'opcodes': [ 0xDDE3 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 129
        "EX (SP), IY":\
        {
            'opcodes': [ 0xFDE3 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 130
        "LDI":\
        {
            'opcodes': [ 0xEDA0 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 132
        "LDIR":\
        {
            'opcodes': [ 0xEDB0 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 134
        "LDD":\
        {
            'opcodes': [ 0xEDA8 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 136
        "LDDR":\
        {
            'opcodes': [ 0xEDB8 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 138
        "CPI":\
        {
            'opcodes': [ 0xEDA1 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 139
        "CPIR":\
        {
            'opcodes': [ 0xED81 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 141
        "CPD":\
        {
            'opcodes': [ 0xEDA9 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 142
        "CPDR":\
        {
            'opcodes': [ 0xEDB9 ],
            'size': 2,
            'operands': [],
        },
        
        
        
        ############################
        ##                        ##
        ## 8-Bit Arithmetic Group ##
        ##                        ##
        ############################
        ## Page 145
        "ADD A, r":\
        {
            'opcodes': [ (0b10000_000 | (i << 0)) for i in r ],
            'size': 1,
            'operands': [ 'r0' ],
        },
        
        ## Page 147
        "ADD A, n":\
        {
            'opcodes': [ 0xC6 ],
            'size': 2,
            'operands': [ 'n' ],
        },
        
        ## Page 148
        "ADD A, (HL)":\
        {
            'opcodes': [ 0x86 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 149
        "ADD A, (IX+d)":\
        {
            'opcodes': [ 0xDD86 ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        ## Page 150
        "ADD A, (IY+d)":\
        {
            'opcodes': [ 0xFD86 ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        
        
        ## Page 151
        "ADC A, r":\
        {
            'opcodes': [ (0b10001_000 | (i << 0)) for i in r ],
            'size': 1,
            'operands': [ 'r0' ],
        },
        
        ## Page 151
        "ADC A, n":\
        {
            'opcodes': [ 0xCE ],
            'size': 2,
            'operands': [ 'n' ],
        },
        
        ## Page 151
        "ADC A, (HL)":\
        {
            'opcodes': [ 0x8E ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 151
        "ADC A, (IX+d)":\
        {
            'opcodes': [ 0xDD8E ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        ## Page 151
        "ADC A, (IY+d)":\
        {
            'opcodes': [ 0xFD8E ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        
        
        ## Page 153
        "SUB r":\
        {
            'opcodes': [ (0b10010_000 | (i << 0)) for i in r ],
            'size': 1,
            'operands': [ 'r0' ],
        },
        
        ## Page 153
        "SUB n":\
        {
            'opcodes': [ 0xD6 ],
            'size': 2,
            'operands': [ 'n' ],
        },
        
        ## Page 153
        "SUB (HL)":\
        {
            'opcodes': [ 0x96 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 153
        "SUB (IX+d)":\
        {
            'opcodes': [ 0xDD96 ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        ## Page 153
        "SUB (IY+d)":\
        {
            'opcodes': [ 0xFD96 ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        
        
        ## Page 155
        "SBC r":\
        {
            'opcodes': [ (0b10011_000 | (i << 0)) for i in r ],
            'size': 1,
            'operands': [ 'r0' ],
        },
        
        ## Page 155
        "SBC n":\
        {
            'opcodes': [ 0xDE ],
            'size': 2,
            'operands': [ 'n' ],
        },
        
        ## Page 155
        "SBC (HL)":\
        {
            'opcodes': [ 0x9E ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 155
        "SBC (IX+d)":\
        {
            'opcodes': [ 0xDD9E ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        ## Page 155
        "SBC (IY+d)":\
        {
            'opcodes': [ 0xFD9E ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        
        
        ## Page 157
        "AND r":\
        {
            'opcodes': [ (0b10100_000 | (i << 0)) for i in r ],
            'size': 1,
            'operands': [ 'r0' ],
        },
        
        ## Page 157
        "AND n":\
        {
            'opcodes': [ 0xE6 ],
            'size': 2,
            'operands': [ 'n' ],
        },
        
        ## Page 157
        "AND (HL)":\
        {
            'opcodes': [ 0xA6 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 157
        "AND (IX+d)":\
        {
            'opcodes': [ 0xDDA6 ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        ## Page 157
        "AND (IY+d)":\
        {
            'opcodes': [ 0xFDA6 ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        
        
        ## Page 159
        "OR r":\
        {
            'opcodes': [ (0b10110_000 | (i << 0)) for i in r ],
            'size': 1,
            'operands': [ 'r0' ],
        },
        
        ## Page 159
        "OR n":\
        {
            'opcodes': [ 0xF6 ],
            'size': 2,
            'operands': [ 'n' ],
        },
        
        ## Page 159
        "OR (HL)":\
        {
            'opcodes': [ 0xB6 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 159
        "OR (IX+d)":\
        {
            'opcodes': [ 0xDDB6 ],
            'size': 1,
            'operands': [ 'd' ],
        },
        
        ## Page 159
        "OR (IY+d)":\
        {
            'opcodes': [ 0xFDB6 ],
            'size': 1,
            'operands': [ 'd' ],
        },
        
        
        
        ## Page 161
        "XOR r'":\
        {
            'opcodes': [ (0b10101_000 | (i << 0)) for i in r ],
            'size': 1,
            'operands': [ 'rprime0' ],
        },
        
        ## Page 161
        "XOR n":\
        {
            'opcodes': [ 0xEE ],
            'size': 2,
            'operands': [ 'n' ],
        },
        
        ## Page 161
        "XOR (HL)":\
        {
            'opcodes': [ 0xAE ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 161
        "XOR (IX+d)":\
        {
            'opcodes': [ 0xDDAE ],
            'size': 2,
            'operands': [ 'd' ],
        },
        
        ## Page 161
        "XOR (IY+d)":\
        {
            'opcodes': [ 0xFDAE ],
            'size': 2,
            'operands': [ 'd' ],
        },
        
        
        
        ## Page 163
        "CP r":\
        {
            'opcodes': [ (0b10111_000 | (i << 0)) for i in r ],
            'size': 1,
            'operands': [ 'r0' ],
        },
        
        ## Page 163
        "CP n":\
        {
            'opcodes': [ 0xFE ],
            'size': 2,
            'operands': [ 'n' ],
        },
        
        ## Page 163
        "CP (HL)":\
        {
            'opcodes': [ 0xBE ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 163
        "CP (IX+d)":\
        {
            'opcodes': [ 0xDDBE ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        ## Page 163
        "CP (IY+d)":\
        {
            'opcodes': [ 0xFDBE ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        
        
        ## Page 165
        "INC r":\
        {
            'opcodes': [ (0b00_000_100 | (i << 3)) for i in r],
            'size': 1,
            'operands': [ 'r3' ],
        },
        
        ## Page 167
        "INC (HL)":\
        {
            'opcodes': [ 0x34 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 168
        "INC (IX+d)":\
        {
            'opcodes': [ 0xDD34 ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        ## Page 169
        "INC (IY+d)":\
        {
            'opcodes': [ 0xFD34 ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        
        
        ## Page 170
        "DEC r":\
        {
            'opcodes': [ (0b00_000_101 | (i << 3)) for i in r],
            'size': 1,
            'operands': [ 'r3' ],
        },
        
        ## Page 170
        "DEC (HL)":\
        {
            'opcodes': [ 0x35 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 170
        "DEC (IX+d)":\
        {
            'opcodes': [ 0xDD35 ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        ## Page 170
        "DEC (IY+d)":\
        {
            'opcodes': [ 0xFD35 ],
            'size': 3,
            'operands': [ 'd' ],
        },
        
        
        
        #######################################################
        ##                                                   ##
        ## General-Purpose Arithmetic and CPU Control Groups ##
        ##                                                   ##
        #######################################################
        ## Page 173
        "DAA":\
        {
            'opcodes': [ 0x27 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 175
        "CPL":\
        {
            'opcodes': [ 0x2F ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 176
        "NEG":\
        {
            'opcodes': [ 0xED44 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 178
        "CCF":\
        {
            'opcodes': [ 0x3F ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 179
        "SCF":\
        {
            'opcodes': [ 0x37 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 180
        "NOP":\
        {
            'opcodes': [ 0x00 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 181
        "HALT":\
        {
            'opcodes': [ 0x76 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 182
        "DI":\
        {
            'opcodes': [ 0xF3 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 183
        "EI":\
        {
            'opcodes': [ 0xFB ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 184
        "IM 0":\
        {
            'opcodes': [ 0xED46 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 185
        "IM 1":\
        {
            'opcodes': [ 0xED56 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 186
        "IM 2":\
        {
            'opcodes': [ 0xED5E ],
            'size': 2,
            'operands': [],
        },
        
        
        
        #############################
        ##                         ##
        ## 16-Bit Arithmetic Group ##
        ##                         ##
        #############################
        ## Page 188
        "ADD HL, ss":\
        {
            'opcodes': [ (0b00_00_1001 | (i << 4)) for i in ss ],
            'size': 1,
            'operands': [ 'ss4' ],
        },
        
        ## Page 190
        "ADC HL, ss":\
        {
            'opcodes': [ (0xED00 | 0b01_00_1010 | (i << 4)) for i in ss ],
            'size': 2,
            'operands': [ 'ss4' ],
        },
        
        ## Page 192
        "SBC HL, ss":\
        {
            'opcodes': [ (0xED00 | 0b01_00_0010 | (i << 4)) for i in ss ],
            'size': 2,
            'operands': [ 'ss4' ],
        },
        
        ## Page 194
        "ADD IX, pp":\
        {
            'opcodes': [ (0xDD00 | 0b00_00_1001 | (i << 4)) for i in pp ],
            'size': 2,
            'operands': [ 'pp4' ],
        },
        
        ## Page 194
        "ADD IY, rr":\
        {
            'opcodes': [ (0xFD00 | 0b00_00_1001 | (i << 4)) for i in rr ],
            'size': 1,
            'operands': [ 'rr4' ],
        },
        
        ## Page 198
        "INC ss":\
        {
            'opcodes': [ (0b00_00_0011 | (i << 4)) for i in ss ],
            'size': 1,
            'operands': [ 'ss4' ],
        },
        
        ## Page 199
        "INC IX":\
        {
            'opcodes': [ 0xDD23 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 200
        "INC IY":\
        {
            'opcodes': [ 0xFD23 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 201
        "DEC ss":\
        {
            'opcodes': [ (0b00_00_1011 | (i << 4)) for i in ss ],
            'size': 1,
            'operands': [ 'ss4' ],
        },
        
        ## Page 202
        "DEC IX":\
        {
            'opcodes': [ 0xDD2B ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 203
        "DEC IY":\
        {
            'opcodes': [ 0xFD2B ],
            'size': 2,
            'operands': [],
        },
        
        
        
        ############################
        ##                        ##
        ## Rotate and Shift Group ##
        ##                        ##
        ############################
        ## Page 205
        "RLCA":\
        {
            'opcodes': [ 0x07 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 207
        "RLA":\
        {
            'opcodes': [ 0x17 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 209
        "RRCA":\
        {
            'opcodes': [ 0x0F ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 211
        "RRA":\
        {
            'opcodes': [ 0x1F ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 213
        "RLC r":\
        {
            #'opcodes': [ (0xCB00 | 0b0000_000 | (i << 0)) for i in r ],
            'opcodes': [ (0xCB00 | 0b0000_000 | (i << 0)) for i in r ],
            'size': 2,
            'operands': [ 'r0' ],
        },
        
        ## Page 215
        "RLC (HL)":\
        {
            'opcodes': [ 0xCB06 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 217
        "RLC (IX+d)":\
        {
            'opcodes': [ 0xDDCB06 ],
            'size': 4,
            'operands': [ 'd' ],
        },
        
        ## Page 219
        "RLC (IY+d)":\
        {
            'opcodes': [ 0xFDCB06 ],
            'size': 4,
            'operands': [ 'd' ],
        },
        
        
        
        ## Page 221
        "RL r":\
        {
            'opcodes': [ (0xCB00 | 0b00010_000 | (i << 0)) for i in r ],
            'size': 2,
            'operands': [ 'r0' ],
        },
        
        ## Page 221
        "RL (HL)":\
        {
            'opcodes': [ 0xCB16 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 221
        "RL (IX+d)":\
        {
            'opcodes': [ 0xDDCB16 ],
            'size': 4,
            'operands': [ 'd' ],
        },
        
        ## Page 221
        "RL (IY+d)":\
        {
            'opcodes': [ 0xFDCB16 ],
            'size': 4,
            'operands': [ 'd' ],
        },
        
        
        
        ## Page 227
        "RR r":\
        {
            ## Wrong opcode in um0080.pdf!!!
            #'opcodes': [ (0xCB00 | 0b00001_000 | (i << 0)) for i in r ],
            'opcodes': [ (0xCB00 | 0b00011_000 | (i << 0)) for i in r ],
            'size': 2,
            'operands': [ 'r0' ],
        },
        
        ## Page 227
        "RR (HL)":\
        {
            'opcodes': [ 0xCB1E ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 227
        "RR (IX+d)":\
        {
            'opcodes': [ 0xDDCB1E ],
            'size': 4,
            'operands': [ 'd' ],
        },
        
        ## Page 227
        "RR (IY+d)":\
        {
            'opcodes': [ 0xFDCB1E ],
            'size': 4,
            'operands': [ 'd' ],
        },
        
        
        
        ## Page 230
        "SLA r":\
        {
            'opcodes': [ (0xCB00 | 0b00100_000 | (i << 0)) for i in r ],
            'size': 2,
            'operands': [ 'r0' ],
        },
        
        ## Page 230
        "SLA (HL)":\
        {
            'opcodes': [ 0xCB26 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 230
        "SLA (IX+d)":\
        {
            'opcodes': [ 0xDDCB26 ],
            'size': 4,
            'operands': [ 'd' ],
        },
        
        ## Page 230
        "SLA (IY+d)":\
        {
            'opcodes': [ 0xFDCB26 ],
            'size': 4,
            'operands': [ 'd' ],
        },
        
        
        
        ## Page 236
        "SRL r":\
        {
            'opcodes': [ (0xCB00 | 0b00111_000 | (i << 0)) for i in r ],
            'size': 2,
            'operands': [ 'r0' ],
        },
        
        ## Page 236
        "SRL (HL)":\
        {
            'opcodes': [ 0xCB3E ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 236
        "SRL (IX+d)":\
        {
            'opcodes': [ 0xDDCB3E ],
            'size': 4,
            'operands': [ 'd' ],
        },
        
        ## Page 236
        "SRL (IY+d)":\
        {
            'opcodes': [ 0xFDCB3E ],
            'size': 4,
            'operands': [ 'd' ],
        },
        
        
        
        ####################################
        ##                                ##
        ## Bit Set, Reset, and Test Group ##
        ##                                ##
        ####################################
        ## Page 243
        "BIT b, r":\
        {
            'opcodes': [ (0xCB00 | 0b01_000_000 | (j << 3) | (i << 0)) for j in b for i in r ],
            'size': 2,
            'operands': [ 'b3', 'r0' ],
        },
        
        ## Page 245
        ## 
        ## FIXME: Page 245 wrongfully does not mention bit 7.
        "BIT b, (HL)":\
        {
            'opcodes': [ (0xCB00 | 0b01_000_110 | (i << 3)) for i in b ],
            'size': 2,
            'operands': [ 'b3' ],
        },
        
        ## Page 247
        "BIT b, (IX+d)":\
        {
            'opcodes': [ (0xDDCB00 | 0b01_000_110 | (i << 3)) for i in b ],
            'size': 4,
            'operands': [ 'b3', 'd' ],
        },
        
        ## Page 249
        "BIT b, (IY+d)":\
        {
            'opcodes': [ (0xFDCB00 | 0b01_000_110 | (i << 3)) for i in b ],
            'size': 4,
            'operands': [ 'b3', 'd' ],
        },
        
        
        
        ## Page 251
        "SET b, r":\
        {
            'opcodes': [ (0xCB00 | 0b11_000_000 | (j << 3) | (i << 0)) for j in b for i in r ],
            'size': 2,
            'operands': [ 'b3', 'r0' ],
        },
        
        ## Page 253
        "SET b, (HL)":\
        {
            'opcodes': [ (0xCB00 | 0b11_000_110 | (i << 3)) for i in b ],
            'size': 2,
            'operands': [ 'b3' ],
        },
        
        ## Page 255
        "SET b, (IX+d)":\
        {
            'opcodes': [ (0xDDCB00 | 0b11_000_110 | (i << 3)) for i in b ],
            'size': 4,
            'operands': [ 'b3', 'd' ],
        },
        
        ## Page 257
        "SET b, (IY+d)":\
        {
            'opcodes': [ (0xFDCB00 | 0b11_000_110 | (i << 3)) for i in b ],
            'size': 4,
            'operands': [ 'b3', 'd' ],
        },
        
        
        
        ################
        ##            ##
        ## Jump Group ##
        ##            ##
        ################
        ## Page 262
        "JP nn":\
        {
            'opcodes': [ 0xC3 ],
            'size': 3,
            'operands': [ 'nn' ],
        },
        
        ## Page 263
        "JP cc, nn":\
        {
            'opcodes': [ (0b11_000_010 | (i << 3)) for i in cc ],
            'size': 3,
            'operands': [ 'cc3', 'nn' ],
        },
        
        ## Page 265
        "JR e":\
        {
            'opcodes': [ 0x18 ],
            'size': 2,
            'operands': [ 'e' ],
        },
        
        ## Page 267
        "JR C, e":\
        {
            'opcodes': [ 0x38 ],
            'size': 2,
            'operands': [ 'e' ],
        },
        
        ## Page 269
        "JR NC, e":\
        {
            'opcodes': [ 0x30 ],
            'size': 2,
            'operands': [ 'e' ],
        },
        
        ## Page 271
        "JR Z, e":\
        {
            'opcodes': [ 0x28 ],
            'size': 2,
            'operands': [ 'e' ],
        },
        
        ## Page 273
        "JR NZ, e":\
        {
            'opcodes': [ 0x20 ],
            'size': 2,
            'operands': [ 'e' ],
        },
        
        ## Page 275
        "JP (HL)":\
        {
            'opcodes': [ 0xE9 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 278
        "DJNZ, e":\
        {
            'opcodes': [ 0x10 ],
            'size': 2,
            'operands': [ 'e' ],
        },
        
        
        
        ###########################
        ##                       ##
        ## Call and Return Group ##
        ##                       ##
        ###########################
        ## Page 281
        "CALL nn":\
        {
            'opcodes': [ 0xCD ],
            'size': 3,
            'operands': [ 'nn' ],
        },
        
        ## Page 283
        "CALL cc, nn":\
        {
            'opcodes': [ (0b11_000_100 | (i << 3)) for i in cc ],
            'size': 3,
            'operands': [ 'cc3', 'nn' ],
        },
        
        ## Page 285
        "RET":\
        {
            'opcodes': [ 0xC9 ],
            'size': 1,
            'operands': [],
        },
        
        ## Page 286
        "RET cc":\
        {
            'opcodes': [ (0b11_000_000 | (i << 3)) for i in cc ],
            'size': 1,
            'operands': [ 'cc3' ],
        },
        
        ## Page 288
        "RETI":\
        {
            'opcodes': [ 0xED4D ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 290
        "RETN":\
        {
            'opcodes': [ 0xED45 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 292
        "RST p":\
        {
            'opcodes': [ (0b11_000_111 | (i << 3)) for i in t ],
            'size': 1,
            'operands': [ 't3' ],
        },
        
        
        
        ############################
        ##                        ##
        ## Input and Output Group ##
        ##                        ##
        ############################
        ## Page 295
        "IN A, (n)":\
        {
            'opcodes': [ 0xDB ],
            'size': 2,
            'operands': [ 'n' ],
        },
        
        ## Page 296
        "IN r, (C)":\
        {
            'opcodes': [ (0xED00 | 0b01_000_000 | (i << 3)) for i in r ],
            'size': 2,
            'operands': [ 'r3' ],
        },
        
        ## Page 298
        "INI":\
        {
            'opcodes': [ 0xEDA2 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 300
        "INIR":\
        {
            'opcodes': [ 0xEDB2 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 302
        "IND":\
        {
            'opcodes': [ 0xEDAA ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 304
        "INDR":\
        {
            'opcodes': [ 0xEDBA ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 306
        "OUT (n), A":\
        {
            'opcodes': [ 0xD3 ],
            'size': 2,
            'operands': [ 'n' ],
        },
        
        ## Page 307
        "OUT (C), r":\
        {
            'opcodes': [ (0xED00 | 0b01_000_001 | (i << 3)) for i in r ],
            'size': 2,
            'operands': [ 'r3' ],
        },
        
        ## Page 309
        "OUTI":\
        {
            'opcodes': [ 0xEDA3 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 311
        "OTIR":\
        {
            'opcodes': [ 0xEDB3 ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 313
        "OUTD":\
        {
            'opcodes': [ 0xEDAB ],
            'size': 2,
            'operands': [],
        },
        
        ## Page 315
        "OTDR":\
        {
            'opcodes': [ 0xEDBB ],
            'size': 2,
            'operands': [],
        },
    }
    
    output = ''
    output += 'from   typing import Self, List, Type\n'
    output += 'import z80.instruction\n'
    for instr_name, instr in instructions.items():
        set_variables = []
        str_args = []
        for operand in instr['operands']:
            first_arg_offset = 1
            if instr['opcodes'][0] > 0xFF:
                ## Note: instruction with a 3 byte opcode, are not special here, 
                ## since the argument comes in between the leading 2 opcode and 
                ## the trailing 1 byte opcode.
                first_arg_offset = 2
            
            if operand == 'b3':
                set_variables.append(f'self._b = (opcode >> 3) & 0x07')
                str_args.append('b={self.b}')
            elif operand == 'cc3':
                set_variables.append(f'self._cc = (opcode >> 3) & 0x07')
                str_args.append('cc={self.cc}')
            elif operand == 'd':
                set_variables.append(f'self._d = self._ram.get_byte(self._PC + 2, signed=False)')
                str_args.append('d={self.d}')
            elif operand == 'dd4':
                set_variables.append(f'self._dd = (opcode >> 4) & 0x03')
                str_args.append('dd={self.dd}')
            elif operand == 'e':
                set_variables.append(f'self._e = self._ram.get_byte(self._PC + {first_arg_offset}, signed=True)')
                set_variables.append(f'self._jump_destination = self._PC + self.size + self.e')
                str_args.append('e={self.e}h')
            elif operand == 'n':
                set_variables.append(f'self._n = self._ram.get_byte(self._PC + {first_arg_offset}, signed=False)')
                str_args.append('n={self.n}')
            elif operand == 'nn':
                set_variables.append(f'self._nn = self._ram.get_word(self._PC + {first_arg_offset})')
                str_args.append('nn={self._nn}')
            elif operand == 'pp4':
                set_variables.append(f'self._pp = (opcode >> 4) & 0x03')
                str_args.append('pp={self.pp}')
            elif operand == 'qq4':
                set_variables.append(f'self._qq = (opcode >> 4) & 0x03')
                str_args.append('qq={self.qq}')
            elif operand == 'r0':
                set_variables.append(f'self._r = (opcode >> 0) & 0x07')
                str_args.append('r={self.r}')
            elif operand == 'r3':
                set_variables.append(f'self._r = (opcode >> 3) & 0x07')
                str_args.append('r={self.r}')
            elif operand == 'rprime0':
                set_variables.append(f'self._rprime = (opcode >> 0) & 0x07')
                str_args.append("r'={self.rprime}")
            elif operand == 'rr4':
                set_variables.append(f'self._rr = (opcode >> 4) & 0x03')
                str_args.append('rr={self.rr}')
            elif operand == 't3':
                set_variables.append(f'self._t = (opcode >> 3) & 0x07')
                str_args.append('t={self._t}, p={self.p}')
            elif operand == 'ss4':
                set_variables.append(f'self._ss = (opcode >> 4) & 0x03')
                str_args.append('ss={self.ss}')
            else:
                raise ValueError(f"Unknown operand name '{operand}'.")
        classname = instr_name.replace(" ", "_").replace('(', 'deref_').replace("'", 'prime').translate({ord(ch):None for ch in ',)'}).replace("+", "_plus_")
        output += '\n'
        output += f'class {classname}(z80.instruction.Instruction):\n'
        output += f'    @classmethod\n'
        output += f'    def name(cls) -> str:\n'
        output += f'        return "{instr_name}"\n'
        output += f'    @classmethod\n'
        output += f'    def opcodes(cls) -> List[int]:\n'
        output +=  '        return ['
        output +=  ', '.join(map(lambda i: f'0x{i:02X}', instr['opcodes']))
        output +=  ']\n'
        output += f'    @property\n'
        output += f'    def size(self: Self) -> int:\n'
        output += f'        return {instr["size"]}\n'
        output += f'    def __str__(self: Self) -> str:\n'
        output += f'        return f"{instr_name};'
        if len(str_args) > 0:
            output += ' '
            output += ', '.join(str_args)
        output += '"'
        output +=  '\n'
        output += f'    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:\n'
        output += f'        super().__init__(registers, ram, opcode)\n'
        if len(set_variables) > 0:
            output += '        '
            output += '\n        '.join(set_variables) + '\n'
        for operand in instr['operands']:
            operand_no_digit = re.sub(r'[0-9]$', '', operand)
            match operand_no_digit:
                case 'b':
                    output += '\n'
                    output += '    @property\n'
                    output += '    def b(self: Self) -> str:\n'
                    output += '        return z80.instruction.FormattingType.b(self._b)\n'
                case 'cc':
                    output += '\n'
                    output += '    @property\n'
                    output += '    def cc(self: Self) -> str:\n'
                    output += '        return z80.instruction.FormattingType.cc(self.cc2name[self._cc])\n'
                case 'd':
                    output += '\n'
                    output += '    @property\n'
                    output += '    def d(self: Self) -> str:\n'
                    output += '        return z80.instruction.FormattingType.d(self._d)\n'
                case 'dd':
                    output += '\n'
                    output += '    @property\n'
                    output += '    def dd(self: Self) -> str:\n'
                    output += '        return z80.instruction.FormattingType.dd(self.dd2name[self._dd])\n'
                case 'e':
                    output += '\n'
                    output += '    @property\n'
                    output += '    def e(self: Self) -> int:\n'
                    output += '        return z80.instruction.FormattingType.e(self._e)\n'
                    output += '\n'
                    output += '    @property\n'
                    output += '    def jump_destination(self: Self) -> str:\n'
                    output += '        return z80.instruction.FormattingType.jp(self._jump_destination)\n'
                case 'n':
                    output += '\n'
                    output += '    @property\n'
                    output += '    def n(self: Self) -> str:\n'
                    output += '        return z80.instruction.FormattingType.n(self._n)\n'
                case 'nn':
                    output += '\n'
                    output += '    @property\n'
                    output += '    def nn(self: Self) -> str:\n'
                    output += '        return z80.instruction.FormattingType.nn(self._nn)\n'
                case 'pp':
                    output += '\n'
                    output += '    @property\n'
                    output += '    def pp(self: Self) -> str:\n'
                    output += '        return z80.instruction.FormattingType.pp(self.pp2name[self._pp])\n'
                case 'qq':
                    output += '\n'
                    output += '    @property\n'
                    output += '    def qq(self: Self) -> str:\n'
                    output += '        return z80.instruction.FormattingType.qq(self.qq2name[self._qq])\n'
                case 'r':
                    output += '\n'
                    output += '    @property\n'
                    output += '    def r(self: Self) -> str:\n'
                    output += '        return z80.instruction.FormattingType.r(self.r2name[self._r])\n'
                case 'rprime':
                    output += '\n'
                    output += '    @property\n'
                    output += '    def rprime(self: Self) -> str:\n'
                    output += '        return z80.instruction.FormattingType.r(self.r2name[self._rprime])\n'
                case 'rr':
                    output += '\n'
                    output += '    @property\n'
                    output += '    def rr(self: Self) -> str:\n'
                    output += '        return z80.instruction.FormattingType.rr(self.rr2name[self._rr])\n'
                case 'ss':
                    output += '\n'
                    output += '    @property\n'
                    output += '    def ss(self: Self) -> str:\n'
                    output += '        return z80.instruction.FormattingType.ss(self.ss2name[self._ss])\n'
                case 't':
                    output += '\n'
                    output += '    @property\n'
                    output += '    def p(self: Self) -> int:\n'
                    output += '        return z80.instruction.FormattingType.p(self.t2p[self._t])\n'
    print(output)
