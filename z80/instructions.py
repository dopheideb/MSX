from   typing import Self, List, Type
import z80.instruction

class LD_r_rprime(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD r, r'"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x47, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x57, 0x58, 0x59, 0x5A, 0x5B, 0x5C, 0x5D, 0x5F, 0x60, 0x61, 0x62, 0x63, 0x64, 0x65, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6F, 0x78, 0x79, 0x7A, 0x7B, 0x7C, 0x7D, 0x7F]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"LD r, r'; r={self.r}, r'={self.rprime}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 3) & 0x07
        self._rprime = (opcode >> 0) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

    @property
    def rprime(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._rprime])

class LD_r_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD r, n"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x06, 0x0E, 0x16, 0x1E, 0x26, 0x2E, 0x3E]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"LD r, n; r={self.r}, n={self.n}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 3) & 0x07
        self._n = self._ram.get_byte(self._PC + 1, signed=False)

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

    @property
    def n(self: Self) -> str:
        return z80.instruction.FormattingType.n(self._n)

class LD_r_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD r, (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x46, 0x4E, 0x56, 0x5E, 0x66, 0x6E, 0x7E]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"LD r, (HL); r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 3) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class LD_r_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD r, (IX+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDD46, 0xDD4E, 0xDD56, 0xDD5E, 0xDD66, 0xDD6E, 0xDD7E]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD r, (IX+d); r={self.r}, d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 3) & 0x07
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class LD_r_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD r, (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFD46, 0xFD4E, 0xFD56, 0xFD5E, 0xFD66, 0xFD6E, 0xFD7E]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD r, (IY+d); r={self.r}, d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 3) & 0x07
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class LD_deref_HL_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (HL), r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x77]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"LD (HL), r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 0) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class LD_deref_IX_plus_d_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (IX+d), r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDD70, 0xDD71, 0xDD72, 0xDD73, 0xDD74, 0xDD75, 0xDD77]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD (IX+d), r; d={self.d}, r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)
        self._r = (opcode >> 0) & 0x07

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class LD_deref_IY_plus_d_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (IY+d), r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFD70, 0xFD71, 0xFD72, 0xFD73, 0xFD74, 0xFD75, 0xFD77]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD (IY+d), r; d={self.d}, r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)
        self._r = (opcode >> 0) & 0x07

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class LD_deref_HL_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (HL), n"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x36]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"LD (HL), n; n={self.n}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._n = self._ram.get_byte(self._PC + 1, signed=False)

    @property
    def n(self: Self) -> str:
        return z80.instruction.FormattingType.n(self._n)

class LD_deref_IX_plus_d_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (IX+d), n"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDD36]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD (IX+d), n; d={self.d}, n={self.n}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)
        self._n = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

    @property
    def n(self: Self) -> str:
        return z80.instruction.FormattingType.n(self._n)

class LD_deref_IY_plus_d_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (IY+d), n"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFD36]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD (IY+d), n; d={self.d}, n={self.n}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)
        self._n = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

    @property
    def n(self: Self) -> str:
        return z80.instruction.FormattingType.n(self._n)

class LD_A_deref_BC(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD A, (BC)"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0x3A]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD A, (nn); nn={self._nn}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._nn = self._ram.get_word(self._PC + 1)

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

class LD_deref_BC_A(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (BC), A"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0x32]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD (nn), A; nn={self._nn}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._nn = self._ram.get_word(self._PC + 1)

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

class LD_A_I(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD A, I"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0x01, 0x11, 0x21, 0x31]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD dd, nn; dd={self.dd}, nn={self._nn}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._dd = (opcode >> 4) & 0x03
        self._nn = self._ram.get_word(self._PC + 1)

    @property
    def dd(self: Self) -> str:
        return z80.instruction.FormattingType.dd(self.dd2name[self._dd])

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

class LD_IX_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD IX, nn"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDD21]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD IX, nn; nn={self._nn}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._nn = self._ram.get_word(self._PC + 2)

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

class LD_IY_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD IY, nn"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFD21]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD IY, nn; nn={self._nn}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._nn = self._ram.get_word(self._PC + 2)

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

class LD_HL_deref_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD HL, (nn)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x2A]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD HL, (nn); nn={self._nn}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._nn = self._ram.get_word(self._PC + 1)

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

class LD_dd_deref_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD dd, (nn)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xED4B, 0xED5B, 0xED6B, 0xED7B]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD dd, (nn); dd={self.dd}, nn={self._nn}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._dd = (opcode >> 4) & 0x03
        self._nn = self._ram.get_word(self._PC + 2)

    @property
    def dd(self: Self) -> str:
        return z80.instruction.FormattingType.dd(self.dd2name[self._dd])

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

class LD_IX_deref_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD IX, (nn)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDD2A]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD IX, (nn); nn={self._nn}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._nn = self._ram.get_word(self._PC + 2)

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

class LD_IY_deref_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD IY, (nn)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFD2A]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD IY, (nn); nn={self._nn}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._nn = self._ram.get_word(self._PC + 2)

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

class LD_deref_nn_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (nn), HL"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x22]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"LD (nn), HL; nn={self._nn}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._nn = self._ram.get_word(self._PC + 1)

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

class LD_deref_nn_dd(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (nn), dd"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xED43, 0xED53, 0xED63, 0xED73]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD (nn), dd; nn={self._nn}, dd={self.dd}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._nn = self._ram.get_word(self._PC + 2)
        self._dd = (opcode >> 4) & 0x03

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

    @property
    def dd(self: Self) -> str:
        return z80.instruction.FormattingType.dd(self.dd2name[self._dd])

class LD_deref_nn_IX(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD (nn), IX"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFD22]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"LD (nn), IX; nn={self._nn}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._nn = self._ram.get_word(self._PC + 2)

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

class LD_SP_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "LD SP, HL"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0xC5, 0xD5, 0xE5, 0xF5]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"PUSH qq; qq={self.qq}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._qq = (opcode >> 4) & 0x03

    @property
    def qq(self: Self) -> str:
        return z80.instruction.FormattingType.qq(self.qq2name[self._qq])

class PUSH_IX(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "PUSH IX"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0xC1, 0xD1, 0xE1, 0xF1]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"POP qq; qq={self.qq}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._qq = (opcode >> 4) & 0x03

    @property
    def qq(self: Self) -> str:
        return z80.instruction.FormattingType.qq(self.qq2name[self._qq])

class POP_IX(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "POP IX"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x87]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"ADD A, r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 0) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class ADD_A_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADD A, n"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xC6]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"ADD A, n; n={self.n}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._n = self._ram.get_byte(self._PC + 1, signed=False)

    @property
    def n(self: Self) -> str:
        return z80.instruction.FormattingType.n(self._n)

class ADD_A_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADD A, (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0xDD86]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"ADD A, (IX+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class ADD_A_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADD A, (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFD86]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"ADD A, (IY+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class ADC_A_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADC A, r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8F]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"ADC A, r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 0) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class ADC_A_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADC A, n"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCE]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"ADC A, n; n={self.n}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._n = self._ram.get_byte(self._PC + 1, signed=False)

    @property
    def n(self: Self) -> str:
        return z80.instruction.FormattingType.n(self._n)

class ADC_A_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADC A, (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0xDD8E]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"ADC A, (IX+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class ADC_A_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADC A, (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFD8E]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"ADC A, (IY+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class SUB_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SUB r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x90, 0x91, 0x92, 0x93, 0x94, 0x95, 0x97]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"SUB r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 0) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class SUB_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SUB n"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xD6]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"SUB n; n={self.n}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._n = self._ram.get_byte(self._PC + 1, signed=False)

    @property
    def n(self: Self) -> str:
        return z80.instruction.FormattingType.n(self._n)

class SUB_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SUB (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x96]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"SUB (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class SUB_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SUB (IX+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDD96]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"SUB (IX+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class SUB_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SUB (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFD96]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"SUB (IY+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class SBC_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SBC r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x98, 0x99, 0x9A, 0x9B, 0x9C, 0x9D, 0x9F]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"SBC r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 0) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class SBC_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SBC n"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDE]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"SBC n; n={self.n}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._n = self._ram.get_byte(self._PC + 1, signed=False)

    @property
    def n(self: Self) -> str:
        return z80.instruction.FormattingType.n(self._n)

class SBC_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SBC (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x9E]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"SBC (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class SBC_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SBC (IX+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDD9E]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"SBC (IX+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class SBC_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SBC (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFD9E]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"SBC (IY+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class AND_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "AND r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5, 0xA7]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"AND r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 0) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class AND_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "AND n"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xE6]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"AND n; n={self.n}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._n = self._ram.get_byte(self._PC + 1, signed=False)

    @property
    def n(self: Self) -> str:
        return z80.instruction.FormattingType.n(self._n)

class AND_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "AND (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0xDDA6]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"AND (IX+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class AND_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "AND (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFDA6]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"AND (IY+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class OR_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "OR r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5, 0xB7]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"OR r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 0) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class OR_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "OR n"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xF6]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"OR n; n={self.n}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._n = self._ram.get_byte(self._PC + 1, signed=False)

    @property
    def n(self: Self) -> str:
        return z80.instruction.FormattingType.n(self._n)

class OR_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "OR (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xB6]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"OR (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class OR_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "OR (IX+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDDB6]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"OR (IX+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class OR_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "OR (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFDB6]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"OR (IY+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class XOR_rprime(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "XOR r'"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD, 0xAF]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"XOR r'; r'={self.rprime}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._rprime = (opcode >> 0) & 0x07

    @property
    def rprime(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._rprime])

class XOR_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "XOR n"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xEE]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"XOR n; n={self.n}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._n = self._ram.get_byte(self._PC + 1, signed=False)

    @property
    def n(self: Self) -> str:
        return z80.instruction.FormattingType.n(self._n)

class XOR_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "XOR (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0xDDAE]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"XOR (IX+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class XOR_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "XOR (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFDAE]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"XOR (IY+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class CP_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CP r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xB8, 0xB9, 0xBA, 0xBB, 0xBC, 0xBD, 0xBF]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"CP r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 0) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class CP_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CP n"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFE]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"CP n; n={self.n}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._n = self._ram.get_byte(self._PC + 1, signed=False)

    @property
    def n(self: Self) -> str:
        return z80.instruction.FormattingType.n(self._n)

class CP_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CP (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0xDDBE]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"CP (IX+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class CP_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CP (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFDBE]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"CP (IY+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class INC_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "INC r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x04, 0x0C, 0x14, 0x1C, 0x24, 0x2C, 0x3C]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"INC r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 3) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class INC_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "INC (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0xDD34]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"INC (IX+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class INC_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "INC (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFD34]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"INC (IY+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class DEC_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "DEC r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x05, 0x0D, 0x15, 0x1D, 0x25, 0x2D, 0x3D]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"DEC r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 3) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class DEC_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "DEC (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0xDD35]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"DEC (IX+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class DEC_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "DEC (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFD35]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"DEC (IY+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class DAA(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "DAA"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x27]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"DAA;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class CPL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CPL"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0xED44]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"NEG;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class CCF(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CCF"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0x09, 0x19, 0x29, 0x39]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"ADD HL, ss; ss={self.ss}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._ss = (opcode >> 4) & 0x03

    @property
    def ss(self: Self) -> str:
        return z80.instruction.FormattingType.ss(self.ss2name[self._ss])

class ADC_HL_ss(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADC HL, ss"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xED4A, 0xED5A, 0xED6A, 0xED7A]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"ADC HL, ss; ss={self.ss}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._ss = (opcode >> 4) & 0x03

    @property
    def ss(self: Self) -> str:
        return z80.instruction.FormattingType.ss(self.ss2name[self._ss])

class SBC_HL_ss(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SBC HL, ss"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xED42, 0xED52, 0xED62, 0xED72]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"SBC HL, ss; ss={self.ss}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._ss = (opcode >> 4) & 0x03

    @property
    def ss(self: Self) -> str:
        return z80.instruction.FormattingType.ss(self.ss2name[self._ss])

class ADD_IX_pp(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADD IX, pp"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDD09, 0xDD19, 0xDD29, 0xDD39]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"ADD IX, pp; pp={self.pp}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._pp = (opcode >> 4) & 0x03

    @property
    def pp(self: Self) -> str:
        return z80.instruction.FormattingType.pp(self.pp2name[self._pp])

class ADD_IY_rr(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "ADD IY, rr"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFD09, 0xFD19, 0xFD29, 0xFD39]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"ADD IY, rr; rr={self.rr}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._rr = (opcode >> 4) & 0x03

    @property
    def rr(self: Self) -> str:
        return z80.instruction.FormattingType.rr(self.rr2name[self._rr])

class INC_ss(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "INC ss"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x03, 0x13, 0x23, 0x33]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"INC ss; ss={self.ss}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._ss = (opcode >> 4) & 0x03

    @property
    def ss(self: Self) -> str:
        return z80.instruction.FormattingType.ss(self.ss2name[self._ss])

class INC_IX(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "INC IX"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDD23]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"INC IX;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class INC_IY(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "INC IY"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFD23]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"INC IY;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class DEC_ss(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "DEC ss"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x0B, 0x1B, 0x2B, 0x3B]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"DEC ss; ss={self.ss}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._ss = (opcode >> 4) & 0x03

    @property
    def ss(self: Self) -> str:
        return z80.instruction.FormattingType.ss(self.ss2name[self._ss])

class DEC_IX(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "DEC IX"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDD2B]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"DEC IX;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class DEC_IY(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "DEC IY"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFD2B]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"DEC IY;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class RLCA(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RLCA"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x07]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"RLCA;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class RLA(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RLA"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x17]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"RLA;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class RRCA(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RRCA"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x0F]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"RRCA;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class RRA(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RRA"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x1F]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"RRA;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class RLC_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RLC r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCB00, 0xCB01, 0xCB02, 0xCB03, 0xCB04, 0xCB05, 0xCB07]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"RLC r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 0) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class RLC_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RLC (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCB06]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"RLC (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class RLC_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RLC (IX+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDDCB06]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"RLC (IX+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class RLC_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RLC (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFDCB06]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"RLC (IY+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class RL_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RL r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCB10, 0xCB11, 0xCB12, 0xCB13, 0xCB14, 0xCB15, 0xCB17]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"RL r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 0) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class RL_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RL (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCB16]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"RL (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class RL_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RL (IX+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDDCB16]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"RL (IX+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class RL_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RL (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFDCB16]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"RL (IY+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class RR_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RR r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCB18, 0xCB19, 0xCB1A, 0xCB1B, 0xCB1C, 0xCB1D, 0xCB1F]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"RR r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 0) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class RR_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RR (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCB1E]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"RR (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class RR_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RR (IX+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDDCB1E]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"RR (IX+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class RR_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RR (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFDCB1E]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"RR (IY+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class SLA_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SLA r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCB20, 0xCB21, 0xCB22, 0xCB23, 0xCB24, 0xCB25, 0xCB27]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"SLA r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 0) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class SLA_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SLA (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCB26]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"SLA (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class SLA_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SLA (IX+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDDCB26]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"SLA (IX+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class SLA_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SLA (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFDCB26]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"SLA (IY+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class SRL_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SRL r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCB38, 0xCB39, 0xCB3A, 0xCB3B, 0xCB3C, 0xCB3D, 0xCB3F]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"SRL r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 0) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class SRL_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SRL (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCB3E]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"SRL (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class SRL_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SRL (IX+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDDCB3E]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"SRL (IX+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class SRL_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SRL (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFDCB3E]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"SRL (IY+d); d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class BIT_b_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "BIT b, r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCB40, 0xCB41, 0xCB42, 0xCB43, 0xCB44, 0xCB45, 0xCB47, 0xCB48, 0xCB49, 0xCB4A, 0xCB4B, 0xCB4C, 0xCB4D, 0xCB4F, 0xCB50, 0xCB51, 0xCB52, 0xCB53, 0xCB54, 0xCB55, 0xCB57, 0xCB58, 0xCB59, 0xCB5A, 0xCB5B, 0xCB5C, 0xCB5D, 0xCB5F, 0xCB60, 0xCB61, 0xCB62, 0xCB63, 0xCB64, 0xCB65, 0xCB67, 0xCB68, 0xCB69, 0xCB6A, 0xCB6B, 0xCB6C, 0xCB6D, 0xCB6F, 0xCB70, 0xCB71, 0xCB72, 0xCB73, 0xCB74, 0xCB75, 0xCB77, 0xCB78, 0xCB79, 0xCB7A, 0xCB7B, 0xCB7C, 0xCB7D, 0xCB7F]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"BIT b, r; b={self.b}, r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._b = (opcode >> 3) & 0x07
        self._r = (opcode >> 0) & 0x07

    @property
    def b(self: Self) -> str:
        return z80.instruction.FormattingType.b(self._b)

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class BIT_b_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "BIT b, (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCB46, 0xCB4E, 0xCB56, 0xCB5E, 0xCB66, 0xCB6E, 0xCB76, 0xCB7E]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"BIT b, (HL); b={self.b}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._b = (opcode >> 3) & 0x07

    @property
    def b(self: Self) -> str:
        return z80.instruction.FormattingType.b(self._b)

class BIT_b_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "BIT b, (IX+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDDCB46, 0xDDCB4E, 0xDDCB56, 0xDDCB5E, 0xDDCB66, 0xDDCB6E, 0xDDCB76, 0xDDCB7E]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"BIT b, (IX+d); b={self.b}, d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._b = (opcode >> 3) & 0x07
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def b(self: Self) -> str:
        return z80.instruction.FormattingType.b(self._b)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class BIT_b_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "BIT b, (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFDCB46, 0xFDCB4E, 0xFDCB56, 0xFDCB5E, 0xFDCB66, 0xFDCB6E, 0xFDCB76, 0xFDCB7E]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"BIT b, (IY+d); b={self.b}, d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._b = (opcode >> 3) & 0x07
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def b(self: Self) -> str:
        return z80.instruction.FormattingType.b(self._b)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class SET_b_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SET b, r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCBC0, 0xCBC1, 0xCBC2, 0xCBC3, 0xCBC4, 0xCBC5, 0xCBC7, 0xCBC8, 0xCBC9, 0xCBCA, 0xCBCB, 0xCBCC, 0xCBCD, 0xCBCF, 0xCBD0, 0xCBD1, 0xCBD2, 0xCBD3, 0xCBD4, 0xCBD5, 0xCBD7, 0xCBD8, 0xCBD9, 0xCBDA, 0xCBDB, 0xCBDC, 0xCBDD, 0xCBDF, 0xCBE0, 0xCBE1, 0xCBE2, 0xCBE3, 0xCBE4, 0xCBE5, 0xCBE7, 0xCBE8, 0xCBE9, 0xCBEA, 0xCBEB, 0xCBEC, 0xCBED, 0xCBEF, 0xCBF0, 0xCBF1, 0xCBF2, 0xCBF3, 0xCBF4, 0xCBF5, 0xCBF7, 0xCBF8, 0xCBF9, 0xCBFA, 0xCBFB, 0xCBFC, 0xCBFD, 0xCBFF]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"SET b, r; b={self.b}, r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._b = (opcode >> 3) & 0x07
        self._r = (opcode >> 0) & 0x07

    @property
    def b(self: Self) -> str:
        return z80.instruction.FormattingType.b(self._b)

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class SET_b_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SET b, (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCBC6, 0xCBCE, 0xCBD6, 0xCBDE, 0xCBE6, 0xCBEE, 0xCBF6, 0xCBFE]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"SET b, (HL); b={self.b}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._b = (opcode >> 3) & 0x07

    @property
    def b(self: Self) -> str:
        return z80.instruction.FormattingType.b(self._b)

class SET_b_deref_IX_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SET b, (IX+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDDCBC6, 0xDDCBCE, 0xDDCBD6, 0xDDCBDE, 0xDDCBE6, 0xDDCBEE, 0xDDCBF6, 0xDDCBFE]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"SET b, (IX+d); b={self.b}, d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._b = (opcode >> 3) & 0x07
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def b(self: Self) -> str:
        return z80.instruction.FormattingType.b(self._b)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class SET_b_deref_IY_plus_d(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "SET b, (IY+d)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xFDCBC6, 0xFDCBCE, 0xFDCBD6, 0xFDCBDE, 0xFDCBE6, 0xFDCBEE, 0xFDCBF6, 0xFDCBFE]
    @property
    def size(self: Self) -> int:
        return 4
    def __str__(self: Self) -> str:
        return f"SET b, (IY+d); b={self.b}, d={self.d}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._b = (opcode >> 3) & 0x07
        self._d = self._ram.get_byte(self._PC + 2, signed=False)

    @property
    def b(self: Self) -> str:
        return z80.instruction.FormattingType.b(self._b)

    @property
    def d(self: Self) -> str:
        return z80.instruction.FormattingType.d(self._d)

class JP_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JP nn"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xC3]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"JP nn; nn={self._nn}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._nn = self._ram.get_word(self._PC + 1)

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

class JP_cc_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JP cc, nn"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xC2, 0xCA, 0xD2, 0xDA, 0xE2, 0xEA, 0xF2, 0xFA]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"JP cc, nn; cc={self.cc}, nn={self._nn}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._cc = (opcode >> 3) & 0x07
        self._nn = self._ram.get_word(self._PC + 1)

    @property
    def cc(self: Self) -> str:
        return z80.instruction.FormattingType.cc(self.cc2name[self._cc])

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

class JR_e(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JR e"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x18]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"JR e; e={self.e}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._e = self._ram.get_byte(self._PC + 1, signed=True)
        self._jump_destination = self._PC + self.size + self.e

    @property
    def e(self: Self) -> int:
        return z80.instruction.FormattingType.e(self._e)

    @property
    def jump_destination(self: Self) -> str:
        return z80.instruction.FormattingType.jp(self._jump_destination)

class JR_C_e(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JR C, e"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x38]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"JR C, e; e={self.e}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._e = self._ram.get_byte(self._PC + 1, signed=True)
        self._jump_destination = self._PC + self.size + self.e

    @property
    def e(self: Self) -> int:
        return z80.instruction.FormattingType.e(self._e)

    @property
    def jump_destination(self: Self) -> str:
        return z80.instruction.FormattingType.jp(self._jump_destination)

class JR_NC_e(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JR NC, e"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x30]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"JR NC, e; e={self.e}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._e = self._ram.get_byte(self._PC + 1, signed=True)
        self._jump_destination = self._PC + self.size + self.e

    @property
    def e(self: Self) -> int:
        return z80.instruction.FormattingType.e(self._e)

    @property
    def jump_destination(self: Self) -> str:
        return z80.instruction.FormattingType.jp(self._jump_destination)

class JR_Z_e(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JR Z, e"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x28]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"JR Z, e; e={self.e}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._e = self._ram.get_byte(self._PC + 1, signed=True)
        self._jump_destination = self._PC + self.size + self.e

    @property
    def e(self: Self) -> int:
        return z80.instruction.FormattingType.e(self._e)

    @property
    def jump_destination(self: Self) -> str:
        return z80.instruction.FormattingType.jp(self._jump_destination)

class JR_NZ_e(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JR NZ, e"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x20]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"JR NZ, e; e={self.e}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._e = self._ram.get_byte(self._PC + 1, signed=True)
        self._jump_destination = self._PC + self.size + self.e

    @property
    def e(self: Self) -> int:
        return z80.instruction.FormattingType.e(self._e)

    @property
    def jump_destination(self: Self) -> str:
        return z80.instruction.FormattingType.jp(self._jump_destination)

class JP_deref_HL(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "JP (HL)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xE9]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"JP (HL);"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class DJNZ_e(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "DJNZ, e"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0x10]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"DJNZ, e; e={self.e}h"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._e = self._ram.get_byte(self._PC + 1, signed=True)
        self._jump_destination = self._PC + self.size + self.e

    @property
    def e(self: Self) -> int:
        return z80.instruction.FormattingType.e(self._e)

    @property
    def jump_destination(self: Self) -> str:
        return z80.instruction.FormattingType.jp(self._jump_destination)

class CALL_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CALL nn"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xCD]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"CALL nn; nn={self._nn}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._nn = self._ram.get_word(self._PC + 1)

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

class CALL_cc_nn(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "CALL cc, nn"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xC4, 0xCC, 0xD4, 0xDC, 0xE4, 0xEC, 0xF4, 0xFC]
    @property
    def size(self: Self) -> int:
        return 3
    def __str__(self: Self) -> str:
        return f"CALL cc, nn; cc={self.cc}, nn={self._nn}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._cc = (opcode >> 3) & 0x07
        self._nn = self._ram.get_word(self._PC + 1)

    @property
    def cc(self: Self) -> str:
        return z80.instruction.FormattingType.cc(self.cc2name[self._cc])

    @property
    def nn(self: Self) -> str:
        return z80.instruction.FormattingType.nn(self._nn)

class RET(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RET"
    @classmethod
    def opcodes(cls) -> List[int]:
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
    def opcodes(cls) -> List[int]:
        return [0xC0, 0xC8, 0xD0, 0xD8, 0xE0, 0xE8, 0xF0, 0xF8]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"RET cc; cc={self.cc}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._cc = (opcode >> 3) & 0x07

    @property
    def cc(self: Self) -> str:
        return z80.instruction.FormattingType.cc(self.cc2name[self._cc])

class RETI(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RETI"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xED4D]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"RETI;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class RETN(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RETN"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xED45]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"RETN;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class RST_p(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "RST p"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xC7, 0xCF, 0xD7, 0xDF, 0xE7, 0xEF, 0xF7, 0xFF]
    @property
    def size(self: Self) -> int:
        return 1
    def __str__(self: Self) -> str:
        return f"RST p; t={self._t}, p={self.p}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._t = (opcode >> 3) & 0x07

    @property
    def p(self: Self) -> int:
        return z80.instruction.FormattingType.p(self.t2p[self._t])

class IN_A_deref_n(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "IN A, (n)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xDB]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"IN A, (n); n={self.n}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._n = self._ram.get_byte(self._PC + 1, signed=False)

    @property
    def n(self: Self) -> str:
        return z80.instruction.FormattingType.n(self._n)

class IN_r_deref_C(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "IN r, (C)"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xED40, 0xED48, 0xED50, 0xED58, 0xED60, 0xED68, 0xED78]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"IN r, (C); r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 3) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class INI(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "INI"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xEDA2]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"INI;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class INIR(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "INIR"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xEDB2]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"INIR;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class IND(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "IND"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xEDAA]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"IND;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class INDR(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "INDR"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xEDBA]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"INDR;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class OUT_deref_n_A(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "OUT (n), A"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xD3]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"OUT (n), A; n={self.n}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._n = self._ram.get_byte(self._PC + 1, signed=False)

    @property
    def n(self: Self) -> str:
        return z80.instruction.FormattingType.n(self._n)

class OUT_deref_C_r(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "OUT (C), r"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xED41, 0xED49, 0xED51, 0xED59, 0xED61, 0xED69, 0xED79]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"OUT (C), r; r={self.r}"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)
        self._r = (opcode >> 3) & 0x07

    @property
    def r(self: Self) -> str:
        return z80.instruction.FormattingType.r(self.r2name[self._r])

class OUTI(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "OUTI"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xEDA3]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"OUTI;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class OTIR(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "OTIR"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xEDB3]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"OTIR;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class OUTD(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "OUTD"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xEDAB]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"OUTD;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

class OTDR(z80.instruction.Instruction):
    @classmethod
    def name(cls) -> str:
        return "OTDR"
    @classmethod
    def opcodes(cls) -> List[int]:
        return [0xEDBB]
    @property
    def size(self: Self) -> int:
        return 2
    def __str__(self: Self) -> str:
        return f"OTDR;"
    def __init__(self: Self, registers: z80.registers.Registers, ram: z80.ram.RAM, opcode: int) -> None:
        super().__init__(registers, ram, opcode)

