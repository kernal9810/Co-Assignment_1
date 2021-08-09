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
        "00010":["mul","A"]
    }

    def getRegister(self, register_bin):
        return Legend.registers[register_bin]

    def setRegister(self,register_bin, register_val):
        Legend.registers[register_bin] = register_val

    def getType(self, s):
        return Legend.function[s][1]

    def getOp(self,s):
        return Legend.registers[s][0]




