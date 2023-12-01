import abc
import collections
import logging
import sys
from   typing import Self, List, Type
import z80.ram
import z80.registers



## The Z80 has instruction classes in which the instruction can be used on a 
## fixed set of registers.
## 
## Example: LD r, n
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



_cc2n =\
{
    0b000: 'NZ',
    0b001: 'Z',
    0b010: 'NC',
    0b011: 'C',
    0b100: 'PO',
    0b101: 'PE',
    0b110: 'P',
    0b111: 'M',
}



## The Z80 has instruction classes in which the instruction can be used on a 
## fixed set of register pairs.
## 
## Example: LD dd, nn
_dd2n =\
{
    0b00: 'BC',
    0b01: 'DE',
    0b10: 'HL',
    0b11: 'SP',
}



## The Z80 has instruction classes in which the instruction can be used on a 
## fixed set of register pairs.
## 
## Example: ADD IX, pp
_pp2n =\
{
    0b00: 'BC',
    0b01: 'DE',
    0b10: 'IX',
    0b11: 'SP',
}



## The Z80 has instruction classes in which the instruction can be used on a 
## fixed set of register pairs.
## 
## Example: PUSH qq
_qq2n =\
{
    0b00: 'BC',
    0b01: 'DE',
    0b10: 'HL',
    0b11: 'AF',
}



## The Z80 has instruction classes in which the instruction can be used on a 
## fixed set of register pairs.
## 
## Example: INC ss
## 
## Note: exactly the same as dd...
_ss2n =\
{
    0b00: 'BC',
    0b01: 'DE',
    0b10: 'HL',
    0b11: 'SP',
}




class Instruction(abc.ABC):
    instruction_sets = collections.defaultdict(list)
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
        self.PC = self._registers.PC
    
    @property
    def opcode(self: Self) -> int: return self._opcode
    
    @classmethod
    @abc.abstractmethod
    def opcodes(self: Self) -> List[int]: pass
    
    @property
    @abc.abstractmethod
    def size(self: Self) -> int: pass
    
    
    
    @classmethod
    def cc2n(cls, cc: int) -> str:
        return _cc2n[cc]
    
    @classmethod
    def dd2n(cls, dd: int) -> str:
        return _dd2n[dd]
    
    @classmethod
    def pp2n(cls, pp: int) -> str:
        return _pp2n[pp]
    
    @classmethod
    def qq2n(cls, qq: int) -> str:
        return _qq2n[qq]
    
    @classmethod
    def r2n(cls, r: int) -> str:
        return _r2n[r]
    
    @classmethod
    def ss2n(cls, ss: int) -> str:
        return _ss2n[ss]



if __name__ == '__main__':
    b = range(8)
    cc = range(8)
    dd = range(4)
    pp = range(4)
    qq = range(4)
    r = [ x for x in range(8) if x != 0b110 ]
    ss = range(4)
    
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
            'operands': [ 'r0', 'd' ],
        },
        
        ## Page 83
        "LD (IY+d), r":\
        {
            'opcodes': [ (0xFD00 | 0b01110_000 | (i << 0)) for i in r ],
            'size': 3,
            'operands': [ 'r0', 'd' ],
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
            'operands': [ 'nn' ],
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
            'operands': [],
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
        
        
        
        ## Page 157
        "AND r":\
        {
            'opcodes': [ (0b10100_000 | (i << 0)) for i in r ],
            'size': 1,
            'operands': [],
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
        "OR r'":\
        {
            'opcodes': [ (0b10110_000 | (i << 0)) for i in r ],
            'size': 1,
            'operands': [ 'rprime0' ],
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
            'size': 1,
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
        ## Page 187
        "ADD HL, ss":\
        {
            'opcodes': [ (0b00_00_1001 | (i << 4)) for i in ss ],
            'size': 1,
            'operands': [ 'ss4' ],
        },
        
        ## Page 194
        "ADD IX, pp":\
        {
            'opcodes': [ (0xDD00 | 0b00_00_1001 | (i << 4)) for i in pp ],
            'size': 1,
            'operands': [ 'pp4' ],
        },
        
        ## Page 198
        "INC ss":\
        {
            'opcodes': [ (0b00_00_0011 | (i << 4)) for i in ss],
            'size': 1,
            'operands': [ 'ss4' ],
        },
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        "BIT b, (HL)":\
        {
            'opcodes': [ (0xCB00 | 0b01_000_110 | (i << 3)) for i in b ],
            'size': 2,
            'operands': [ 'b3' ],
        },
        
        "BIT b, (IX+d)":\
        {
            'opcodes': [ 0xDDCB ],
            'size': 4,
            'operands': [ 'd', 'b3' ],
        },
        
        "BIT b, (IY+d)":\
        {
            'opcodes': [ 0xFDCB ],
            'size': 4,
            'operands': [ 'd', 'b3' ],
        },
        
        "BIT b, r":\
        {
            'opcodes': [ (0xCB00 | 0b01_000_000 | (j << 3) | (i << 0)) for j in b for i in r ],
            'size': 2,
            'operands': [ 'b3', 'r0' ],
        },
        
        "CALL cc, nn":\
        {
            'opcodes': [ (0b11_000_100 | (i << 3)) for i in r],
            'size': 3,
            'operands': [ 'nn' ],
        },
        
        "CALL nn":\
        {
            'opcodes': [ 0xCD ],
            'size': 3,
            'operands': [ 'nn' ],
        },
        
        
        "DEC ss":\
        {
            'opcodes': [ (0b00_00_1011 | (i << 4)) for i in ss ],
            'size': 1,
            'operands': [ 'ss4' ],
        },
        
        "DJNZ, e":\
        {
            'opcodes': [ 0x10 ],
            'size': 2,
            'operands': [ 'e' ],
        },
        
        
        "JP cc, nn":\
        {
            'opcodes': [ (0b11_000_010 | (i << 3)) for i in cc ],
            'size': 3,
            'operands': [ 'cc3', 'nn' ],
        },
        
        "JP (HL)":\
        {
            'opcodes': [ 0xE9 ],
            'size': 1,
            'operands': [],
        },
        
        "JP nn":\
        {
            'opcodes': [ 0xC3 ],
            'size': 3,
            'operands': [ 'nn' ],
        },
        
        "JR C, e":\
        {
            'opcodes': [ 0x38 ],
            'size': 2,
            'operands': [ 'e' ],
        },
        
        "JR e":\
        {
            'opcodes': [ 0x18 ],
            'size': 2,
            'operands': [ 'e' ],
        },
        
        "JR NC, e":\
        {
            'opcodes': [ 0x30 ],
            'size': 2,
            'operands': [ 'e' ],
        },
        
        "JR NZ, e":\
        {
            'opcodes': [ 0x20 ],
            'size': 2,
            'operands': [ 'e' ],
        },
        
        "JR Z, e":\
        {
            'opcodes': [ 0x28 ],
            'size': 2,
            'operands': [ 'e' ],
        },
        
        "LD (IX), nn":\
        {
            'opcodes': [ 0xDD21 ],
            'size': 4,
            'operands': [ 'nn' ],
        },
        
        "RET":\
        {
            'opcodes': [ 0xC9 ],
            'size': 1,
            'operands': [],
        },
        
        "RET cc":\
        {
            'opcodes': [ (0b11_000_000 | (i << 3)) for i in cc ],
            'size': 1,
            'operands': [ 'cc3' ],
        },
        
        "RLCA":\
        {
            'opcodes': [ 0x07 ],
            'size': 1,
            'operands': [],
        },
        
        "RRA":\
        {
            'opcodes': [ 0x1F ],
            'size': 1,
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
            if operand == 'b3':
                set_variables.append(f'self.b = (opcode >> 3) & 0x07')
                str_args.append('b={self.b}')
            elif operand == 'cc3':
                set_variables.append(f'self.cc = (opcode >> 3) & 0x07')
                str_args.append('cc={self.cc2n(self.cc)}')
            elif operand == 'd':
                set_variables.append(f'self.d = self._ram.get_byte(self.PC + 2, signed=False)')
                str_args.append('d={self.d:02X}h')
            elif operand == 'dd4':
                set_variables.append(f'self.dd = (opcode >> 4) & 0x03')
                str_args.append('dd={self.dd2n(self.dd)}')
            elif operand == 'e':
                set_variables.append(f'self.e  = self._ram.get_byte(self.PC + 1, signed=True)')
                str_args.append('e={self.e:02X}h')
            elif operand == 'n':
                set_variables.append(f'self.n = self._ram.get_byte(self.PC + 1, signed=False)')
                str_args.append('n={self.n:02X}h')
            elif operand == 'nn':
                set_variables.append(f'self.nn = self._ram.get_word(self.PC + 1)')
                str_args.append('nn={self.nn:04X}h')
            elif operand == 'pp4':
                set_variables.append(f'self.pp = (opcode >> 4) & 0x03')
                str_args.append('pp={self.pp2n(self.pp)}')
            elif operand == 'qq4':
                set_variables.append(f'self.qq = (opcode >> 4) & 0x03')
                str_args.append('qq={self.qq2n(self.qq)}')
            elif operand == 'r0':
                set_variables.append(f'self.r = (opcode >> 0) & 0x07')
                str_args.append('r={self.r2n(self.r)}')
            elif operand == 'r3':
                set_variables.append(f'self.r = (opcode >> 3) & 0x07')
                str_args.append('r={self.r2n(self.r)}')
            elif operand == 'rprime0':
                set_variables.append(f'self.rprime = (opcode >> 0) & 0x07')
                str_args.append("r'={self.r2n(self.rprime)}")
            elif operand == 'ss4':
                set_variables.append(f'self.ss = (opcode >> 4) & 0x03')
                str_args.append('ss={self.ss2n(self.ss)}')
            else:
                raise ValueError(f"Unknown operand name '{operand}'.")
        classname = instr_name.replace(" ", "_").replace('(', 'deref_').replace("'", 'prime').translate({ord(ch):None for ch in ',)'}).replace("+", "_plus_")
        output += '\n'
        output += f'class {classname}(z80.instruction.Instruction):\n'
        output += f'    @classmethod\n'
        output += f'    def name(cls) -> str:\n'
        output += f'        return "{instr_name}"\n'
        output += f'    @classmethod\n'
        output += f'    def opcodes(self: Self) -> List[int]:\n'
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
    print(output)
