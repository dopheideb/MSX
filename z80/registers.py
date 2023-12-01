import logging
from   typing import Self
#import z80.register


class RegPair:
    def __init__(self: Self) -> None:
        self._l = 0x00
        self._h = 0x00
    
    @property
    def h(self: Self) -> int:
        return self._h
    @h.setter
    def h(self: Self, value: int) -> None:
        if value < 0 or value > 0xFF:
            raise ValueError
        self._h = value

    
    @property
    def l(self: Self) -> int:
        return self._l
    @l.setter
    def l(self: Self, value: int) -> None:
        if value < 0 or value > 0xFF:
            raise ValueError
        self._l = value



class Registers:
    def __init__(self: Self):
        self._AF = RegPair()
        self._BC = RegPair()
        self._DE = RegPair()
        self._HL = RegPair()
        self._PC = RegPair()
        self._SP = RegPair()
    
    
    
    @property
    def A(self: Self) -> int:
        return self._AF.h
    @A.setter
    def A(self: Self, value: int) -> None:
        self._AF.h = value
    
    
    
    @property
    def B(self: Self) -> int:
        return self._BC.l
    @B.setter
    def B(self: Self, value: int) -> None:
        self._BC.l = value
    
    
    
    @property
    def BC(self: Self) -> int:
        return (self._BC.h << 8) | (self._BC.l)
    @BC.setter
    def BC(self: Self, value: int) -> None:
        self._BC.h = value >> 8
        self._BC.l = value & 0xFF
    
    
    
    @property
    def DE(self: Self) -> int:
        return (self._DE.h << 8) | (self._DE.l)
    @DE.setter
    def DE(self: Self, value: int) -> None:
        self._DE.h = value >> 8
        self._DE.l = value & 0xFF
    
    
    
    @property
    def H(self: Self) -> int:
        return self._HL.h
    @H.setter
    def H(self: Self, value: int) -> None:
        self._HL.h = value
    
    
    
    @property
    def HL(self: Self) -> int:
        return (self._HL.h << 8) | (self._HL.l)
    @HL.setter
    def HL(self: Self, value: int) -> None:
        self._HL.h = value >> 8
        self._HL.l = value & 0xFF
    
    
    
    @property
    def L(self: Self) -> int:
        return self._HL.l
    @L.setter
    def L(self: Self, value: int) -> None:
        self._HL.l = value
    
    
    
    @property
    def PC(self: Self) -> int:
        return (self._PC.h << 8) | (self._PC.l)
    @PC.setter
    def PC(self: Self, value: int) -> None:
        self._PC.h = value >> 8
        self._PC.l = value & 0xFF
    
    
    
    def set_r_n(self: Self, r: int, n: int) -> None:
        match r:
            case 0b000:
                self.B = n
            case 0b001:
                self.C = n
            case 0b010:
                self.D = n
            case 0b011:
                self.E = n
            case 0b100:
                self.H = n
            case 0b101:
                self.L = n
            
            case 0b111:
                self.A = n
            case _:
                raise ValueError(f'register value {r:#05b} is not a known register.')
    
    def get_reg_dd(self: Self, dd: int) -> RegPair:
        if dd == 0b00:
            return self._BC
        if dd == 0b00:
            return self._DE
        if dd == 0b10:
            return self._HL
        if dd == 0b11:
            return self._SP
        raise ValueError
    
    def set_reg_dd(self: Self, dd: int, value: int) -> None:
        if dd == 0b00:
            self.BC = value; return
        if dd == 0b01:
            self.DE = value; return
        if dd == 0b10:
            self.HL = value; return
        if dd == 0b11:
            self.SP = value; return
        raise ValueError
