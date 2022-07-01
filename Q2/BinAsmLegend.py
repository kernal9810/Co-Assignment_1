class Legend:

    registers = {
        "000": "0000000000000000",
        "001": "0000000000000000",
        "010": "0000000000000000",
        "011": "0000000000000000",
        "100": "0000000000000000",
        "101": "0000000000000000",
        "110": "0000000000000000",
        "111": "0000000000000000",
    }

    function = {
        "00000": ["add", "A"],
        "00001": ["sub", "A"],
        "00010": ["mov_im", "B"],
        "00011": ["mov", "C"],
        "00100": ["ld", "D"],
        "00101": ["st", "D"],
        "00110": ["mul", "A"],
        "00111": ["div", "C"],
        "01000": ["Rshift", "B"],
        "01001": ["Lshift", "B"],
        "01010": ["xor", "A"],
        "01011": ["or", "A"],
        "01100": ["and", "A"],
        "01101": ["not", "C"],
        "01110": ["cmp", "C"],
        "01111": ["jmp", "E"],
        "10000": ["jlt", "E"],
        "10001": ["jgt", "E"],
        "10010": ["je", "E"],
        "10011": ["hlt", "F"]
    }

    @staticmethod
    def getRegister(register_bin):
        return Legend.registers[register_bin]

    @staticmethod
    def setRegister(register_bin, register_val):
        Legend.registers[register_bin] = register_val

    @staticmethod
    def getType(s):
        return Legend.function[s][1]

    @staticmethod
    def getOp(s):
        return Legend.registers[s][0]




