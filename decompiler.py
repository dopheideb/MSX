#!/usr/bin/env python3

import abc
from   functools import partial
import logging
import os
from   typing import Self, Tuple
import z80
import z80.disasm.instruction
import z80.registers

logging.basicConfig(level=logging.DEBUG)



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
    msx.cpu.override_instruction(z80.disasm.instruction.CALL_nn)
    msx.cpu.set_ram(bytes=rom, offset=0x4000)
    #msx.cpu.PC = 0x4000
    msx.cpu.PC = 0x404F
    
    if True:
        for i in range(17):
            msx.stepi()
    sys.exit(42)
