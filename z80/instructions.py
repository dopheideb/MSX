from   typing import Self, List, Type
import z80.instruction

class LD_r_rprime(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD r, r'"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x47, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x57, 0x58, 0x59, 0x5A, 0x5B, 0x5C, 0x5D, 0x5F, 0x60, 0x61, 0x62, 0x63, 0x64, 0x65, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6F, 0x78, 0x79, 0x7A, 0x7B, 0x7C, 0x7D, 0x7F]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"LD r, r'; r={self.r2n(self.r)}, r'={self.r2n(self.rprime)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.r = (opcode >> 3) & 0x07
        self.rprime = (opcode >> 0) & 0x07

class LD_r_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD r, n"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x06, 0x0E, 0x16, 0x1E, 0x26, 0x2E, 0x3E]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"LD r, n; r={self.r2n(self.r)}, n={self.n:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.r = (opcode >> 3) & 0x07
        self.n = self._ram.get_byte(self.PC + 1, signed=False)

class LD_r_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD r, (HL)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x46, 0x4E, 0x56, 0x5E, 0x66, 0x6E, 0x7E]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"LD r, (HL); r={self.r2n(self.r)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.r = (opcode >> 3) & 0x07

class LD_r_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD r, (IX+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDD46, 0xDD4E, 0xDD56, 0xDD5E, 0xDD66, 0xDD6E, 0xDD7E]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD r, (IX+d); r={self.r2n(self.r)}, d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.r = (opcode >> 3) & 0x07
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class LD_r_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD r, (IY+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFD46, 0xFD4E, 0xFD56, 0xFD5E, 0xFD66, 0xFD6E, 0xFD7E]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD r, (IY+d); r={self.r2n(self.r)}, d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.r = (opcode >> 3) & 0x07
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class LD_deref_HL_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (HL), r"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x77]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"LD (HL), r; r={self.r2n(self.r)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.r = (opcode >> 0) & 0x07

class LD_deref_IX_plus_d_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (IX+d), r"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDD70, 0xDD71, 0xDD72, 0xDD73, 0xDD74, 0xDD75, 0xDD77]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD (IX+d), r; r={self.r2n(self.r)}, d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.r = (opcode >> 0) & 0x07
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class LD_deref_IY_plus_d_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (IY+d), r"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFD70, 0xFD71, 0xFD72, 0xFD73, 0xFD74, 0xFD75, 0xFD77]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD (IY+d), r; r={self.r2n(self.r)}, d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.r = (opcode >> 0) & 0x07
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class LD_deref_HL_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (HL), n"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x36]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"LD (HL), n; n={self.n:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.n = self._ram.get_byte(self.PC + 1, signed=False)

class LD_deref_IX_plus_d_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (IX+d), n"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDD36]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD (IX+d), n; d={self.d:02X}h, n={self.n:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)
        self.n = self._ram.get_byte(self.PC + 1, signed=False)

class LD_deref_IY_plus_d_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (IY+d), n"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFD36]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD (IY+d), n; d={self.d:02X}h, n={self.n:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)
        self.n = self._ram.get_byte(self.PC + 1, signed=False)

class LD_A_deref_BC(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD A, (BC)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x0A]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"LD A, (BC);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class LD_A_deref_DE(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD A, (DE)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x1A]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"LD A, (DE);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class LD_A_deref_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD A, (nn)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x3A]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD A, (nn); nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.nn = self._ram.get_word(self.PC + 1)

class LD_deref_BC_A(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (BC), A"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x02]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"LD (BC), A;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class LD_deref_DE_A(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (DE), A"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x12]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"LD (DE), A;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class LD_deref_nn_A(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (nn), A"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x32]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD (nn), A; nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.nn = self._ram.get_word(self.PC + 1)

class LD_A_I(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD A, I"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xED57]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"LD A, I;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class LD_A_R(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD A, R"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xED5F]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"LD A, R;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class LD_I_A(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD I, A"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xED47]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"LD I, A;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class LD_R_A(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD R, A"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xED4F]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"LD R, A;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class LD_dd_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD dd, nn"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x01, 0x11, 0x21, 0x31]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD dd, nn; dd={self.dd2n(self.dd)}, nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.dd = (opcode >> 4) & 0x03
        self.nn = self._ram.get_word(self.PC + 1)

class LD_IX_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD IX, nn"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDD21]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD IX, nn; nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.nn = self._ram.get_word(self.PC + 1)

class LD_IY_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD IY, nn"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFD21]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD IY, nn; nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.nn = self._ram.get_word(self.PC + 1)

class LD_HL_deref_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD HL, (nn)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x2A]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD HL, (nn); nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.nn = self._ram.get_word(self.PC + 1)

class LD_dd_deref_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD dd, (nn)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xED4B, 0xED5B, 0xED6B, 0xED7B]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD dd, (nn); dd={self.dd2n(self.dd)}, nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.dd = (opcode >> 4) & 0x03
        self.nn = self._ram.get_word(self.PC + 1)

class LD_IX_deref_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD IX, (nn)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDD2A]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD IX, (nn); nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.nn = self._ram.get_word(self.PC + 1)

class LD_IY_deref_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD IY, (nn)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFD2A]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD IY, (nn); nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.nn = self._ram.get_word(self.PC + 1)

class LD_deref_nn_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (nn), HL"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x22]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD (nn), HL; nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.nn = self._ram.get_word(self.PC + 1)

class LD_deref_nn_dd(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (nn), dd"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xED43, 0xED53, 0xED63, 0xED73]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD (nn), dd; nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.nn = self._ram.get_word(self.PC + 1)

class LD_deref_nn_IX(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (nn), IX"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFD22]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD (nn), IX; nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.nn = self._ram.get_word(self.PC + 1)

class LD_SP_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD SP, HL"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xF9]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"LD SP, HL;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class LD_SP_IX(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD SP, IX"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDDF9]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"LD SP, IX;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class LD_SP_IY(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD SP, IY"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFDF9]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"LD SP, IY;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class PUSH_qq(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "PUSH qq"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xC5, 0xD5, 0xE5, 0xF5]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"PUSH qq; qq={self.qq2n(self.qq)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.qq = (opcode >> 4) & 0x03

class PUSH_IX(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "PUSH IX"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDDE5]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"PUSH IX;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class PUSH_IY(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "PUSH IY"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFDE5]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"PUSH IY;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class POP_qq(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "POP qq"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xC1, 0xD1, 0xE1, 0xF1]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"POP qq; qq={self.qq2n(self.qq)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.qq = (opcode >> 4) & 0x03

class POP_IX(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "POP IX"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDDE1]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"POP IX;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class POP_IY(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "POP IY"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFDE1]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"POP IY;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class EX_DE_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "EX DE, HL"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xEB]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"EX DE, HL;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class EX_AF_AFprime(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "EX AF, AF'"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x08]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"EX AF, AF';"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class EXX(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "EXX"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xD9]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"EXX;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class EX_deref_SP_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "EX (SP), HL"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xE3]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"EX (SP), HL;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class EX_deref_SP_IX(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "EX (SP), IX"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDDE3]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"EX (SP), IX;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class EX_deref_SP_IY(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "EX (SP), IY"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFDE3]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"EX (SP), IY;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class LDI(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LDI"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xEDA0]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"LDI;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class LDIR(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LDIR"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xEDB0]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"LDIR;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class LDD(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LDD"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xEDA8]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"LDD;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class LDDR(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LDDR"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xEDB8]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"LDDR;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class CPI(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CPI"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xEDA1]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"CPI;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class CPIR(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CPIR"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xED81]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"CPIR;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class CPD(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CPD"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xEDA9]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"CPD;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class CPDR(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CPDR"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xEDB9]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"CPDR;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class ADD_A_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADD A, r"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x87]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"ADD A, r; r={self.r2n(self.r)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.r = (opcode >> 0) & 0x07

class ADD_A_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADD A, n"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xC6]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"ADD A, n; n={self.n:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.n = self._ram.get_byte(self.PC + 1, signed=False)

class ADD_A_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADD A, (HL)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x86]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"ADD A, (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class ADD_A_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADD A, (IX+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDD86]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"ADD A, (IX+d); d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class ADD_A_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADD A, (IY+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFD86]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"ADD A, (IY+d); d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class ADC_A_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADC A, r"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8F]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"ADC A, r;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class ADC_A_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADC A, n"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xCE]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"ADC A, n; n={self.n:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.n = self._ram.get_byte(self.PC + 1, signed=False)

class ADC_A_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADC A, (HL)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x8E]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"ADC A, (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class ADC_A_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADC A, (IX+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDD8E]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"ADC A, (IX+d); d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class ADC_A_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADC A, (IY+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFD8E]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"ADC A, (IY+d); d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class AND_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "AND r"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5, 0xA7]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"AND r;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class AND_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "AND n"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xE6]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"AND n; n={self.n:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.n = self._ram.get_byte(self.PC + 1, signed=False)

class AND_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "AND (HL)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xA6]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"AND (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class AND_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "AND (IX+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDDA6]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"AND (IX+d); d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class AND_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "AND (IY+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFDA6]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"AND (IY+d); d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class OR_rprime(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "OR r'"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5, 0xB7]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"OR r'; r'={self.r2n(self.rprime)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.rprime = (opcode >> 0) & 0x07

class XOR_rprime(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "XOR r'"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD, 0xAF]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"XOR r'; r'={self.r2n(self.rprime)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.rprime = (opcode >> 0) & 0x07

class XOR_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "XOR n"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xEE]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"XOR n; n={self.n:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.n = self._ram.get_byte(self.PC + 1, signed=False)

class XOR_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "XOR (HL)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xAE]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"XOR (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class XOR_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "XOR (IX+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDDAE]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"XOR (IX+d); d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class XOR_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "XOR (IY+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFDAE]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"XOR (IY+d); d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class CP_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CP r"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xB8, 0xB9, 0xBA, 0xBB, 0xBC, 0xBD, 0xBF]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"CP r; r={self.r2n(self.r)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.r = (opcode >> 0) & 0x07

class CP_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CP n"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFE]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"CP n; n={self.n:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.n = self._ram.get_byte(self.PC + 1, signed=False)

class CP_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CP (HL)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xBE]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"CP (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class CP_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CP (IX+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDDBE]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"CP (IX+d); d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class CP_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CP (IY+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFDBE]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"CP (IY+d); d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class INC_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "INC r"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x04, 0x0C, 0x14, 0x1C, 0x24, 0x2C, 0x3C]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"INC r; r={self.r2n(self.r)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.r = (opcode >> 3) & 0x07

class INC_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "INC (HL)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x34]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"INC (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class INC_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "INC (IX+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDD34]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"INC (IX+d); d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class INC_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "INC (IY+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFD34]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"INC (IY+d); d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class DEC_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "DEC r"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x05, 0x0D, 0x15, 0x1D, 0x25, 0x2D, 0x3D]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"DEC r; r={self.r2n(self.r)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.r = (opcode >> 3) & 0x07

class DEC_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "DEC (HL)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x35]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"DEC (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class DEC_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "DEC (IX+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDD35]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"DEC (IX+d); d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class DEC_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "DEC (IY+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFD35]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"DEC (IY+d); d={self.d:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)

class CPL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CPL"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x2F]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"CPL;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class NEG(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "NEG"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xED44]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"NEG;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class CCF(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CCF"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x3F]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"CCF;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class SCF(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SCF"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x37]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"SCF;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class NOP(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "NOP"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x00]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"NOP;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class HALT(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "HALT"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x76]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"HALT;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class DI(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "DI"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xF3]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"DI;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class EI(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "EI"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFB]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"EI;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class IM_0(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "IM 0"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xED46]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"IM 0;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class IM_1(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "IM 1"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xED56]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"IM 1;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class IM_2(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "IM 2"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xED5E]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"IM 2;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class ADD_HL_ss(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADD HL, ss"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x09, 0x19, 0x29, 0x39]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"ADD HL, ss; ss={self.ss2n(self.ss)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.ss = (opcode >> 4) & 0x03

class ADD_IX_pp(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADD IX, pp"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDD09, 0xDD19, 0xDD29, 0xDD39]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"ADD IX, pp; pp={self.pp2n(self.pp)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.pp = (opcode >> 4) & 0x03

class INC_ss(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "INC ss"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x03, 0x13, 0x23, 0x33]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"INC ss; ss={self.ss2n(self.ss)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.ss = (opcode >> 4) & 0x03

class BIT_b_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "BIT b, (HL)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xCB46, 0xCB4E, 0xCB56, 0xCB5E, 0xCB66, 0xCB6E, 0xCB76, 0xCB7E]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"BIT b, (HL); b={self.b}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.b = (opcode >> 3) & 0x07

class BIT_b_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "BIT b, (IX+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDDCB]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"BIT b, (IX+d); d={self.d:02X}h, b={self.b}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)
        self.b = (opcode >> 3) & 0x07

class BIT_b_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "BIT b, (IY+d)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xFDCB]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"BIT b, (IY+d); d={self.d:02X}h, b={self.b}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.d = self._ram.get_byte(self.PC + 2, signed=False)
        self.b = (opcode >> 3) & 0x07

class BIT_b_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "BIT b, r"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xCB40, 0xCB41, 0xCB42, 0xCB43, 0xCB44, 0xCB45, 0xCB47, 0xCB48, 0xCB49, 0xCB4A, 0xCB4B, 0xCB4C, 0xCB4D, 0xCB4F, 0xCB50, 0xCB51, 0xCB52, 0xCB53, 0xCB54, 0xCB55, 0xCB57, 0xCB58, 0xCB59, 0xCB5A, 0xCB5B, 0xCB5C, 0xCB5D, 0xCB5F, 0xCB60, 0xCB61, 0xCB62, 0xCB63, 0xCB64, 0xCB65, 0xCB67, 0xCB68, 0xCB69, 0xCB6A, 0xCB6B, 0xCB6C, 0xCB6D, 0xCB6F, 0xCB70, 0xCB71, 0xCB72, 0xCB73, 0xCB74, 0xCB75, 0xCB77, 0xCB78, 0xCB79, 0xCB7A, 0xCB7B, 0xCB7C, 0xCB7D, 0xCB7F]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"BIT b, r; b={self.b}, r={self.r2n(self.r)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.b = (opcode >> 3) & 0x07
        self.r = (opcode >> 0) & 0x07

class CALL_cc_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CALL cc, nn"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xC4, 0xCC, 0xD4, 0xDC, 0xE4, 0xEC, 0xFC]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"CALL cc, nn; nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.nn = self._ram.get_word(self.PC + 1)

class CALL_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CALL nn"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xCD]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"CALL nn; nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.nn = self._ram.get_word(self.PC + 1)

class DEC_ss(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "DEC ss"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x0B, 0x1B, 0x2B, 0x3B]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"DEC ss; ss={self.ss2n(self.ss)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.ss = (opcode >> 4) & 0x03

class DJNZ_e(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "DJNZ, e"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x10]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"DJNZ, e; e={self.e:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.e  = self._ram.get_byte(self.PC + 1, signed=True)

class JP_cc_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JP cc, nn"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xC2, 0xCA, 0xD2, 0xDA, 0xE2, 0xEA, 0xF2, 0xFA]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"JP cc, nn; cc={self.cc2n(self.cc)}, nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.cc = (opcode >> 3) & 0x07
        self.nn = self._ram.get_word(self.PC + 1)

class JP_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JP (HL)"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xE9]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"JP (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class JP_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JP nn"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xC3]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"JP nn; nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.nn = self._ram.get_word(self.PC + 1)

class JR_C_e(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JR C, e"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x38]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"JR C, e; e={self.e:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.e  = self._ram.get_byte(self.PC + 1, signed=True)

class JR_e(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JR e"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x18]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"JR e; e={self.e:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.e  = self._ram.get_byte(self.PC + 1, signed=True)

class JR_NC_e(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JR NC, e"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x30]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"JR NC, e; e={self.e:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.e  = self._ram.get_byte(self.PC + 1, signed=True)

class JR_NZ_e(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JR NZ, e"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x20]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"JR NZ, e; e={self.e:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.e  = self._ram.get_byte(self.PC + 1, signed=True)

class JR_Z_e(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JR Z, e"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x28]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"JR Z, e; e={self.e:02X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.e  = self._ram.get_byte(self.PC + 1, signed=True)

class LD_deref_IX_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (IX), nn"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xDD21]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD (IX), nn; nn={self.nn:04X}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.nn = self._ram.get_word(self.PC + 1)

class RET(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RET"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xC9]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"RET;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class RET_cc(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RET cc"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0xC0, 0xC8, 0xD0, 0xD8, 0xE0, 0xE8, 0xF0, 0xF8]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"RET cc; cc={self.cc2n(self.cc)}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self.cc = (opcode >> 3) & 0x07

class RLCA(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RLCA"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x07]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"RLCA;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class RRA(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RRA"
    @classmethod
    def opcodes(self: Self) -> List[int]:
        return [0x1F]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"RRA;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

