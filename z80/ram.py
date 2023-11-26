from   typing import Self, Iterable, Union, SupportsIndex, Any

class RAM:
    def __init__(self: Self, size: int=128*1024):
        self._ram = bytearray(size)
    
    def __getitem__(self: Self, key: Union[int, SupportsIndex]) -> int:
        return self._ram[key]
    
    def __setitem__(self: Self, key: Any, value: Union[int, bytes]) -> None:
        self._ram[key] = value
    
    
    
    def get_byte(self: Self, offset: int) -> int:
        return self._ram[offset]
    
    def get_word(self: Self, offset: int) -> int:
        return (
            self._ram[offset]
            |
            (self._ram[offset + 1] << 8)
        )
