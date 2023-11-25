#!/usr/bin/env python3

import abc
from   functools import partial
import logging
import os
from   typing import Optional, Self, Tuple
import z80
import z80.registers

logging.basicConfig(level=logging.DEBUG)



class CommonOpcodeData:
    def __init__(self: Self, opcode: int, addr: int, next_byte: int, next_word: int) -> None:
        self._opcode = opcode
        self._addr   = addr
        self._byte = next_byte
        self._word = next_word
    
    @property
    def opcode(self: Self): return self._opcode
    @property
    def addr(self: Self): return self._addr
    @property
    def n(self: Self): return self._byte
    @property
    def byte(self: Self): return self._byte
    @property
    def nn(self: Self): return self._word
    @property
    def word(self: Self): return self._word



class AbstractDecompilerWriter(abc.ABC):
    def __init__(self: Self) -> None:
        pass
    
    ####
    ## Data/meta
    ####
    @abc.abstractmethod
    def defb(self: Self, byte: int) -> str: pass
    
    @abc.abstractmethod
    def defw(self: Self, word: int) -> str: pass
    
    @abc.abstractmethod
    def origin(self: Self, origin: int) -> str: pass
    
    
    ####
    ## Actual opcodes.
    ####
    @abc.abstractmethod
    def BIT_b_deref_HL(self: Self, c: CommonOpcodeData, bit: int) -> str: pass
    
    @abc.abstractmethod
    def CALL_nn(self: Self, c: CommonOpcodeData) -> str: pass
    
    @abc.abstractmethod
    def DI(self: Self, c: CommonOpcodeData) -> str: pass
    
    @abc.abstractmethod
    def JP_nn(self: Self, c: CommonOpcodeData) -> str: pass
    
    @abc.abstractmethod
    def LD_HL_deref_nn(self: Self, c: CommonOpcodeData) -> str: pass
    
    @abc.abstractmethod
    def LD_HL_nn(self: Self, c: CommonOpcodeData) -> str: pass
    
    @abc.abstractmethod
    def LD_r_HL(self: Self, c: CommonOpcodeData, r: str) -> str: pass
    
    @abc.abstractmethod
    def LD_r_n(self: Self, c: CommonOpcodeData, r: str) -> str: pass
    
    @abc.abstractmethod
    def LD_r_rprime(self: Self, c: CommonOpcodeData) -> str: pass
    
    @abc.abstractmethod
    def NOP(self: Self, c: CommonOpcodeData) -> str: pass
    
    @abc.abstractmethod
    def RET(self: Self, c: CommonOpcodeData) -> str: pass

class Opcode(abc.ABC):
    @property
    @abc.abstractmethod
    def ids(self: Self) -> [int]: pass
    
    @property
    @abc.abstractmethod
    def size(self: Self) -> int: pass

class LD_r_rprime(Opcode):
    def id(self: Self) -> [int]: return [0x80, 0x81, 0x82]
    def size(self: Self) -> int: return 1
class RET(Opcode):
    def id(self: Self) -> [int]: return [0xC9]
    def size(self: Self) -> int: return 1



class Z80dasm2023Formatter(AbstractDecompilerWriter):
    def __init__(self: Self) -> None:
        super().__init__()
        self.indent = '\t'
    
    def origin(self: Self, origin: int) -> str:
        return f'\torg\t{origin:05x}h'
    
    def defb(self: Self, byte: int) -> str:
        return 'STUB'
    
    def defw(self: Self, word: int) -> str:
        return 'STUB'
    
    
    
    def BIT_b_deref_HL(self: Self, c: CommonOpcodeData, bit: int) -> str:
        return f'{self.indent}bit {bit},(hl)\t\t;{addr:04x}'
    
    def CALL_nn(self: Self, c: CommonOpcodeData) -> str:
        return f'{self.indent}call {c.nn:05x}h\t\t;{c.addr:04x}'
    
    def DI(self: Self, c: CommonOpcodeData) -> str:
        return f'{self.indent}di\t\t\t;{c.addr:04x}'
    
    def JP_nn(self: Self, c: CommonOpcodeData) -> str:
        return f'{self.indent}jp {c.nn:05x}h\t\t;{c.addr:04x}'
    
    def LD_HL_deref_nn(self: Self, c: CommonOpcodeData) -> str:
        return f'{self.indent}ld hl,({c.nn:05x})\t\t;{c.addr:04x}'
    
    def LD_HL_nn(self: Self, c: CommonOpcodeData) -> str:
        return f'{self.indent}ld hl,{c.nn:05x}\t\t;{c.addr:04x}'
    
    def LD_r_HL(self: Self, c: CommonOpcodeData, r: str) -> str:
        return f'{self.indent}ld {r.lower()},(hl)\t\t\t;{c.addr:04x}'
    
    def LD_r_n(self: Self, c: CommonOpcodeData, r: str) -> str:
        return f'{self.indent}ld {r.lower()},{c.n:03x}h\t\t\t;{c.addr:04x}'
    
    def LD_r_rprime(self: Self, c: CommonOpcodeData, r: str, rprime: str) -> str:
        return f'{self.indent}ld {r.lower()},{rprime.lower()}\t\t\t;{c.addr:04x}'
    
    def NOP(self: Self, c: CommonOpcodeData) -> str:
        return f'{self.indent}nop\t\t\t;{c.addr:04x}'
    
    def RET(self: Self, c: CommonOpcodeData) -> str:
        return f'{self.indent}ret\t\t\t;{c.addr:04x}'



class Decompiler:
    def __init__(self: Self, binary: bytes=b'', origin: int=0x4000) -> None:
        self.binary = binary
        self.origin = origin
        
        self.detect_cartridge = False
        self.sep = os.linesep
        self.indent = '    '
        
        self.template_address = '0x{:04X}'
        self.template_byte = '0x{:02X}'
        self.template_disasm_address = '{:04X}'
        self.template_label = '{1:04x}_{0:s}:'
        self.template_word = '0x{:04X}'
        
        self.formatter = Z80dasm2023Formatter()
        self.style = 'z80dasm2023'
        if self.style == 'z80dasm2023':
            self.template_address = '0x{:04X}'
            self.template_byte = '0x{:02X}'
            self.template_disasm_address = '{:04X}'
            self.template_label = '{1:04x}_{0:s}:'
            self.template_word = '0x{:04X}'

        #self.A = None
    
    def set_binary(self: Self, binary: bytes) -> Self:
        self.binary = binary
        return self
    
    def set_origin(self: Self, origin: int) -> Self:
        self.origin = origin
        return self
    
    def format_as_address(self: Self, address: int) -> str:
        return self.template_address.format(address)
    
    def format_as_byte(self: Self, byte: int) -> str:
        return self.template_byte.format(byte)
    
    def format_as_disasm_address(self: Self, address: int) -> str:
        return self.template_disasm_address.format(address)
    
    def format_as_label(self: Self, address: int, offset:int) -> str:
        return self.template_label.format(address, offset)
    
    def format_as_word(self: Self, word: int) -> str:
        return self.template_word.format(word)
    
    def gen_label(self: Self, label: str, offset: int|None=None) -> str:
        if offset is None:
            offset = self.offset
        memory_address = self.origin + offset
        return self.format_as_label(label, memory_address)
    
    def gen_defm(self: Self, defm: str, offset: int|None=None, comment: str='') -> str:
        if offset is None:
            offset = self.offset
        memory_address = self.origin + offset
        return (
            f'{self.indent}defm "{defm}"' +
            f'\t\t; {memory_address:{self.address_format}} {comment}')
    
    def gen_defw(self: Self, defw: int, offset: int|None=None, comment: str='') -> str:
        if offset is None:
            offset = self.offset
        memory_address = self.origin + offset
        output = (
            f'{self.indent}defw {self.format_as_word(defw)}' +
            f'\t\t; {self.format_as_address(memory_address)}')
        if comment != '':
            output += comment
        return output
    
    def get_byte(self: Self, offset: int|None=None) -> int:
        if offset is None:
            offset = self.offset
        return self.binary[offset]
    def get_word(self: Self, offset: int|None=None) -> int:
        if offset is None:
            offset = self.offset
        return (self.binary[offset]) | (self.binary[offset + 1] << 8)
    
    
    
    def decompile(self: Self) -> str:
        output = ''
        
        self.offset = 0
        self.entrypoint = self.origin
        ## 0x4241 is "AB" (in little endian)
        if (self.detect_cartridge
                and
                self.get_word() == 0x4241
                and
                ## Only decode as cartridge if binary is a multiple of 
                ## 16K, i.e. very likely to be a cartridge.
                len(self.binary) & 0x3FFF == 0):
            
            output += self.gen_label('cartridge header')
            output += self.sep
            
            output += self.gen_defm('AB', None, 'ID. Must be "AB" for cartridge.')
            output += self.sep
            self.offset += 2
            
            self.entrypoint = self.get_word()
            output += self.gen_defw(self.entrypoint, None , 'INIT. Entry point.')
            output += self.sep
            self.offset += 2
            
            output += self.gen_defw(self.get_word(), None, 'STATEMENT.')
            output += self.sep
            self.offset += 2
            
            output += self.gen_defw(self.get_word(), None, 'DEVICE.')
            output += self.sep
            self.offset += 2
            
            output += self.gen_defw(self.get_word(), None, 'TEXT.')
            output += self.sep
            self.offset += 2
            
            output += self.gen_defw(self.get_word(), None, 'RESERVED FOR FUTURE USE.')
            output += self.sep
            self.offset += 2
            
            output += self.gen_defw(self.get_word(), None, 'RESERVED FOR FUTURE USE.')
            output += self.sep
            self.offset += 2
            
            output += self.gen_defw(self.get_word(), None, 'RESERVED FOR FUTURE USE.')
            output += self.sep
            self.offset += 2
            output += self.sep
        self.offset = self.entrypoint - self.origin
        
        output += self.gen_label('entry_point') + self.sep
        
        while self.offset < len(self.binary):
            memory_address = self.origin + self.offset
            (num, text) = self.decode_opcode_at()
            output += text + self.sep
            self.offset += num
        return output
    
    def decode_opcode_at(self: Self) -> Tuple[str, str, int]:
        opcode_size = 1
        opcode = self.get_byte()
        if opcode == 0xCB or opcode == 0xED:
            opcode_size = 2
            opcode <<= 8
            opcode |= self.get_byte(self.offset + 1)
        
        addr = self.origin + self.offset
        
        next_byte = None
        next_word = None
        try:
            next_byte = self.get_byte(self.offset + opcode_size)
            next_word = self.get_word(self.offset + opcode_size)
        except IndexError:
            ## We can't read beyond end of file.
            pass
        
        cod = CommonOpcodeData(opcode=opcode, addr=addr, next_byte=next_byte, next_word=next_word)
        
        ## Readability is important. What is more readable? Compact 
        ## code, i.e. use masks to compactly code similar opcodes. Or is 
        ## a long list more readable? Both could work here I guess.
        opcode_handlers =\
        {
            0x00: (1, partial(self.formatter.NOP,         c=cod)),
            0x06: (2, partial(self.formatter.LD_r_n,      c=cod, r='B')),
            
            0x0E: (2, partial(self.formatter.LD_r_n,      c=cod, r='C')),
            
            0x16: (2, partial(self.formatter.LD_r_n,      c=cod, r='D')),
            
            0x1E: (2, partial(self.formatter.LD_r_n,      c=cod, r='E')),
            
            0x21: (3, partial(self.formatter.LD_HL_nn,    c=cod)),
            0x26: (2, partial(self.formatter.LD_r_n,      c=cod, r='H')),
            
            0x2A: (3, partial(self.formatter.LD_HL_deref_nn, c=cod)),
            0x2E: (2, partial(self.formatter.LD_r_n,      c=cod, r='L')),



            0x40: (1, partial(self.formatter.LD_r_rprime, c=cod, r='B', rprime='B')),
            0x41: (1, partial(self.formatter.LD_r_rprime, c=cod, r='B', rprime='C')),
            0x42: (1, partial(self.formatter.LD_r_rprime, c=cod, r='B', rprime='D')),
            0x43: (1, partial(self.formatter.LD_r_rprime, c=cod, r='B', rprime='E')),
            0x44: (1, partial(self.formatter.LD_r_rprime, c=cod, r='B', rprime='H')),
            0x45: (1, partial(self.formatter.LD_r_rprime, c=cod, r='B', rprime='L')),
            0x46: (1, partial(self.formatter.LD_r_HL    , c=cod, r='B')),
            0x47: (1, partial(self.formatter.LD_r_rprime, c=cod, r='B', rprime='A')),
            
            0x48: (1, partial(self.formatter.LD_r_rprime, c=cod, r='C', rprime='B')),
            0x49: (1, partial(self.formatter.LD_r_rprime, c=cod, r='C', rprime='C')),
            0x4A: (1, partial(self.formatter.LD_r_rprime, c=cod, r='C', rprime='D')),
            0x4B: (1, partial(self.formatter.LD_r_rprime, c=cod, r='C', rprime='E')),
            0x4C: (1, partial(self.formatter.LD_r_rprime, c=cod, r='C', rprime='H')),
            0x4D: (1, partial(self.formatter.LD_r_rprime, c=cod, r='C', rprime='L')),
            0x4E: (1, partial(self.formatter.LD_r_HL    , c=cod, r='C')),
            0x4F: (1, partial(self.formatter.LD_r_rprime, c=cod, r='C', rprime='A')),
            
            0x50: (1, partial(self.formatter.LD_r_rprime, c=cod, r='D', rprime='B')),
            0x51: (1, partial(self.formatter.LD_r_rprime, c=cod, r='D', rprime='C')),
            0x52: (1, partial(self.formatter.LD_r_rprime, c=cod, r='D', rprime='D')),
            0x53: (1, partial(self.formatter.LD_r_rprime, c=cod, r='D', rprime='E')),
            0x54: (1, partial(self.formatter.LD_r_rprime, c=cod, r='D', rprime='H')),
            0x55: (1, partial(self.formatter.LD_r_rprime, c=cod, r='D', rprime='L')),
            0x56: (1, partial(self.formatter.LD_r_HL    , c=cod, r='D')),
            0x57: (1, partial(self.formatter.LD_r_rprime, c=cod, r='D', rprime='A')),
            
            0x58: (1, partial(self.formatter.LD_r_rprime, c=cod, r='E', rprime='B')),
            0x59: (1, partial(self.formatter.LD_r_rprime, c=cod, r='E', rprime='C')),
            0x5A: (1, partial(self.formatter.LD_r_rprime, c=cod, r='E', rprime='D')),
            0x5B: (1, partial(self.formatter.LD_r_rprime, c=cod, r='E', rprime='E')),
            0x5C: (1, partial(self.formatter.LD_r_rprime, c=cod, r='E', rprime='H')),
            0x5D: (1, partial(self.formatter.LD_r_rprime, c=cod, r='E', rprime='L')),
            0x5E: (1, partial(self.formatter.LD_r_HL    , c=cod, r='E')),
            0x5F: (1, partial(self.formatter.LD_r_rprime, c=cod, r='E', rprime='A')),
            
            0x60: (1, partial(self.formatter.LD_r_rprime, c=cod, r='H', rprime='B')),
            0x61: (1, partial(self.formatter.LD_r_rprime, c=cod, r='H', rprime='C')),
            0x62: (1, partial(self.formatter.LD_r_rprime, c=cod, r='H', rprime='D')),
            0x63: (1, partial(self.formatter.LD_r_rprime, c=cod, r='H', rprime='E')),
            0x64: (1, partial(self.formatter.LD_r_rprime, c=cod, r='H', rprime='H')),
            0x65: (1, partial(self.formatter.LD_r_rprime, c=cod, r='H', rprime='L')),
            0x66: (1, partial(self.formatter.LD_r_HL    , c=cod, r='H')),
            0x67: (1, partial(self.formatter.LD_r_rprime, c=cod, r='H', rprime='A')),
            
            0x68: (1, partial(self.formatter.LD_r_rprime, c=cod, r='L', rprime='B')),
            0x69: (1, partial(self.formatter.LD_r_rprime, c=cod, r='L', rprime='C')),
            0x6A: (1, partial(self.formatter.LD_r_rprime, c=cod, r='L', rprime='D')),
            0x6B: (1, partial(self.formatter.LD_r_rprime, c=cod, r='L', rprime='E')),
            0x6C: (1, partial(self.formatter.LD_r_rprime, c=cod, r='L', rprime='H')),
            0x6D: (1, partial(self.formatter.LD_r_rprime, c=cod, r='L', rprime='L')),
            0x6E: (1, partial(self.formatter.LD_r_HL    , c=cod, r='L')),
            0x6F: (1, partial(self.formatter.LD_r_rprime, c=cod, r='L', rprime='A')),
            
            0x78: (1, partial(self.formatter.LD_r_rprime, c=cod, r='A', rprime='B')),
            0x79: (1, partial(self.formatter.LD_r_rprime, c=cod, r='A', rprime='C')),
            0x7A: (1, partial(self.formatter.LD_r_rprime, c=cod, r='A', rprime='D')),
            0x7B: (1, partial(self.formatter.LD_r_rprime, c=cod, r='A', rprime='E')),
            0x7C: (1, partial(self.formatter.LD_r_rprime, c=cod, r='A', rprime='H')),
            0x7D: (1, partial(self.formatter.LD_r_rprime, c=cod, r='A', rprime='L')),
            0x7E: (1, partial(self.formatter.LD_r_HL    , c=cod, r='A')),
            0x7F: (1, partial(self.formatter.LD_r_rprime, c=cod, r='A', rprime='A')),
            
            0xC3: (3, partial(self.formatter.JP_nn,       c=cod)),
            
            0xCD: (3, partial(self.formatter.CALL_nn,     c=cod)),
            
            0xC9: (1, partial(self.formatter.RET, c=cod)),
            
            0xF3: (1, partial(self.formatter.DI, c=cod)),
        }
        
        if opcode in opcode_handlers:
            (num, func) = opcode_handlers[opcode]
            return (num, func())
        


        
        
        
        
        
        
        
        if opcode == 0b_1100_1101: ## 0xCB
            return self.handle_CB_bit_instructions()
        
        return (1, '0x{:02X}'.format(opcode))
    
    def handle_CB_bit_instructions(self: Self) -> str:
        return (2, '???')
    
    
    
    def opcode_IM(self: Self) -> Tuple[int, str, str]:
        operand = self.binary[self.offset + 1]
        operand2modenum =\
        {
            0x46: 0,
            0x56: 1,
            0x5E: 2,
        }
        try:
            modenum = operand2modenum[operand]
            im_text = f'im {modenum}'
            comment = f'Set Interrupt Mode {modenum}'
        except KeyError:
            im_text = 'im ?'
            comment = 'UNKNOWN INTERRUPT MODE'
        return (2, im_text, comment)
    
    def opcode_LD_n_A(self: Self) -> Tuple[int, str, str]:
        nn = self.get_word(self.offset + 1)
        comment = ''
        if nn == 0xFD9A:
            comment = 'H.KEYI[0] = A'
        return (3, f'*({self.format_as_address(nn)}) = A', comment)
    
    def opcode_LD_nn_HL(self: Self) -> Tuple[int, str, str]:
        nn = self.get_word(self.offset + 1)
        comment = ''
        if nn == 0xFD9B:
            comment = 'H.KEYI[1] = L, H.KEYI[2] = H'
        return (3, f'*({self.format_as_address(nn)}) = HL', comment)

class TMS9918:
    def __init__(self: Self):
        self.vram = bytearray(16 * 1024)

class MSX:
    def __init__(self: Self):
        self._vdp = TMS9918()
        self._cpu = z80.Z80()
    
    @property
    def cpu(self: Self) -> z80.Z80:
        return self._cpu
    
    def stepi(self: Self):
        self._cpu.stepi()


if __name__ == '__main__':
    import sys
    rom = open(sys.argv[1], 'rb').read()
    
    msx = MSX()
    #msx.cpu.PC = 0x4000
    msx.cpu.PC = 0x404F
    msx.cpu.set_ram(bytes=rom, offset=0x4000)
    
    if True:
        for i in range(17):
            msx.stepi()
    sys.exit(42)
    
    print(Decompiler(binary=rom).decompile())
    output = 'exception caught'
    try:
        output = Decompiler(binary=rom).decompile()
    except ValueError:
        ## Ignore for now.
        pass
    print(output)
