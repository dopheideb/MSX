from   typing import Self

class RAM:
    def __init__(self: Self, size: int=128*1024):
        self._ram = bytearray(size)
    
    def __getitem__(self: Self, key: int) -> int:
        return self._ram[key]
    
    def __setitem__(self: Self, key: int, value: int) -> None:
        self._ram[key] = value
    
    
    
    def get_byte(self: Self, offset: int) -> int:
        return self._ram[offset]
    
    def get_word(self: Self, offset: int) -> int:
        return (
            self._ram[offset]
            |
            (self._ram[offset + 1] << 8)
        )
