import collections
import logging
import struct
from   typing import Self, Iterable, List, Union, SupportsIndex, Any

class RAM:
    def __init__(self: Self, size: int=128*1024) -> None:
        ## Question: Why do we use a list and not bytearray(size)?
        ## 
        ## Answer: We want to be able to store the None value, which a bytearray does not 
        ## accept.
        ## 
        ## Question: Why do we want to store None?
        ## 
        ## Answer: handy for a disassembler: it can use it to detect fixed values (if the 
        ## disassemblers uses None for a non fixed value).
        #self._ram = bytearray(size)
        self._ram: List[Union[int, None]] = [None] * size
        self._write_callback: dict = collections.defaultdict(list)
    
    def __getitem__(self: Self, key: Union[int, SupportsIndex]) -> Union[int, None]:
        return self._ram[key]
    
    def __setitem__(self: Self, key: int, value: Union[int, None]) -> None:
        if value is not None:
            ## The bytes object does all the type and range checking for us.
            b = bytes([value])
        
        old_value = self._ram[key]
        self._ram[key] = value
        
        if key in self._write_callback:
            for func in self._write_callback[key]:
                logging.debug(f'Calling write callback {func} with old_value={old_value}')
                func(key, value, old_value)
    
    
    
    def get_byte(self: Self, offset: int, signed=False) -> Union[int, None]:
        b = self._ram[offset]
        if b is None:
            return ValueError(f'Tried to read from uninitialized memory at offset=0x{offset:04X}.')
        
        if not signed:
            ## Unsigned
            return b
        
        if not b & 0x80:
            ## Signed, but no sign bit (i.e. positive).
            return b
        
        ## Signed, with sign bit enabled (i.e. negative).
        return -128 + (b & 0x7F)
    
    def get_word(self: Self, offset: int) -> Union[int, None]:
        b1 = self._ram[offset + 0]
        b2 = self._ram[offset + 1]
        if b1 is None or b2 is None:
            return None
        
        return b1 | (b2 << 8)
    
    def set_word(self: Self, offset: int, value: int) -> None:
        self[offset + 0] = value & 0x00FF
        self[offset + 1] = value >> 8
    
    def register_write_callback(self: Self, func, location) -> None:
        self._write_callback[location].append(func)
