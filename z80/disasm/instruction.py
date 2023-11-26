import logging
from   typing import Self
import z80.instruction

class CALL_nn(z80.instruction.CALL_nn):
    def __str__(self: Self) -> str:
        return f'en hoe komen we hier dan?'

