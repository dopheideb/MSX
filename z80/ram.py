import collections
import logging
import struct
from   typing import Self, Iterable, Union, SupportsIndex, Any

class RAM:
    def __init__(self: Self, size: int=128*1024):
        self._ram = bytearray(size)
        self._write_callback = collections.defaultdict(list)
    
    def __getitem__(self: Self, key: Union[int, SupportsIndex]) -> int:
        return self._ram[key]
    
    def __setitem__(self: Self, key: Any, value: Union[int, bytes]) -> None:
        old_value = self._ram[key]
        self._ram[key] = value
        if isinstance(key, int):
            if key in self._write_callback:
                for func in self._write_callback[key]:
                    logging.debug(f'Calling write callback {func} with old_value={old_value}')
                    func(key, value, old_value)
    
    
    
    def get_byte(self: Self, offset: int, signed=False) -> int:
        b = self._ram[offset]
        if not signed:
            ## Unsigned
            return b
        if not b & 0x80:
            ## Signed, but no sign bit (i.e. positive).
            return b
        return -128 + (b & 0x7F)
    
    def get_word(self: Self, offset: int) -> int:
        return (
            self._ram[offset]
            |
            (self._ram[offset + 1] << 8)
        )
    
    def register_write_callback(self: Self, func, location) -> None:
        self._write_callback[location].append(func)
