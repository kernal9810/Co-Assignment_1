import sys
import matplotlib
from matplotlib import pyplot as plt

mem_dump = ["0"*16]*256

def main():

    global mem_dump
    halt = False
    pc = 0
    complete_input = sys.stdin.read()
    Mem = (complete_input.split("\n"))

    for i in range(len(Mem)):
        mem_dump[i] = Mem[i]

    while not halt:
        line = Mem[pc]

        halt, new_pc = executeLine(line, pc)

        print(format(pc, "08b") + " " + Legend.registers["000"] + " " + Legend.registers["001"] + " " + Legend.registers["010"] + " " +
               Legend.registers["011"] + " " +  Legend.registers["100"] + " " +  Legend.registers["101"] +  " " + Legend.registers["110"] + " " +
               Legend.registers["111"])

        pc = new_pc

    for i in mem_dump:
        print(i)

list= []
def executeLine(ins, pc):
    global mem_dump

    halt = False

    list.append(pc)
    type = Legend.getType(ins[:5])

    if type == "A":
        ExecuteEngine.Ex_typeA(ins)
        pc += 1
    elif type == "B":
        ExecuteEngine.Ex_typeB(ins)
        pc += 1
    elif type == "C":
        ExecuteEngine.Ex_typeC(ins)
        pc += 1
    elif type == "D":
        mem_dump = ExecuteEngine.Ex_typeD(ins, pc, mem_dump)
        pc += 1
    elif type == "E":
        pc = ExecuteEngine.Ex_typeE(ins, pc)
    elif type == "F":
        halt = True
        pc = 0
    return halt, pc



class ExecuteEngine:

    @staticmethod
    def checkOverflow(r_value):
        flag = Legend.getRegister("111")
        if len(r_value) > 16:
            r_value = r_value[len(r_value) - 16:]
            flag = flag[:12] + "1" + flag[13:16]
        else:
            flag = flag[:12] + "0" + flag[13:16]

        Legend.setRegister("111", flag)
        return r_value

    @staticmethod
    def flagReset():
        flag = Legend.getRegister("111")
        flag = flag[:12] + "0000"

        Legend.setRegister("111", flag)

    @staticmethod
    def Ex_typeA(ins):
        ExecuteEngine.flagReset()

        r = ins[7:10]
        b = int(Legend.getRegister(ins[10:13]),2)
        c = int(Legend.getRegister(ins[13:16]),2)

        op = Legend.getOp(ins[:5])

        if op == "mul":
            Legend.setRegister(r, "0"*8 + format(int(b * c), "08b"))
            Legend.setRegister(r,ExecuteEngine.checkOverflow(Legend.getRegister(r)))

        elif op == "add":
            Legend.setRegister(r, "0"*8 + format(int(b + c), "08b"))
            Legend.setRegister(r,ExecuteEngine.checkOverflow(Legend.getRegister(r)))

        elif op == "sub":
            Legend.setRegister(r, "0"*8 + format(int(b - c), "08b"))
            Legend.setRegister(r,ExecuteEngine.checkOverflow(Legend.getRegister(r)))

        elif op == "xor":
            Legend.setRegister(r, "0"*8 + format(int(b ^ c), "08b"))

        elif op == "and":
            Legend.setRegister(r, "0"*8 + format(int(b and c), "08b"))

        elif op == "or":
            Legend.setRegister(r, "0"*8 + format(int(b or c), "08b"))

    @staticmethod
    def Ex_typeB(ins):

        ExecuteEngine.flagReset()

        r = ins[5:8]
        r_val = int(Legend.getRegister(r), 2)
        b = int((ins[8:16]),2)

        op = Legend.getOp(ins[:5])
        if op == "mov_im":
            Legend.setRegister(r, "0"*8 + format(int(b), "08b"))

        elif op == "Lshift":
            Legend.setRegister(r, "0"*8 + format(int(r_val << b), "08b"))
        elif op == "Rshift":
            Legend.setRegister(r, "0"*8 + format(int(r_val >> b), "08b"))

    @staticmethod
    def Ex_typeC(ins):

        r = ins[10:13]
        r_1 = int(Legend.getRegister(r),2)
        r_2 = Legend.getRegister(ins[13:16])


        b = int(r_2,2)

        op = Legend.getOp(ins[:5])

        if op == "mov":
            Legend.setRegister(r, r_2)
            ExecuteEngine.flagReset()

        elif op == "div":
            ExecuteEngine.flagReset()
            q = "0"*8 + format(int(r_1 / b), "08b")
            rem = "0"*8 + format(int(r_1 % b), "08b")

            Legend.setRegister("000", q)
            Legend.setRegister("001", rem)

        elif op == "not":
            ExecuteEngine.flagReset()
            invert = ""
            for i in r_2:
                if i == "1":
                    invert += "0"
                else:
                    invert += "1"
            Legend.setRegister(r, invert)

        elif op == "cmp":
            ExecuteEngine.flagReset()
            flag = Legend.getRegister("111")
            fl = 0
            fe = 0
            fg = 0

            if int(r_1) > b:
                fg = 1
            elif int(r_1) < b:
                fl = 1
            else:
                fe = 1
            flag = flag[:13] + str(fl) + str(fg) + str(fe)

            Legend.setRegister("111", flag)

    @staticmethod
    def Ex_typeD(ins, pc, mem_dump):
        ExecuteEngine.flagReset()

        r = ins[5:8]
        op = Legend.getOp(ins[:5])
        address = int(ins[8:],2)


        if op == "st":
            r_value = Legend.getRegister(ins[5:8])
            mem_dump[address] = "0"*8 + format(int(r_value,2), "08b")
        

        if op == "ld":
            Legend.setRegister(r, "0"*8 + format(int(mem_dump[address],2), "08b"))
            # print("0"*8 + format(mem_dump[address],"08b"))

        return mem_dump


    @staticmethod
    def Ex_typeE(ins, pc):

        flag = Legend.getRegister("111")
        fl = flag[13]
        fg = flag[14]
        fe = flag[15]

        op = Legend.getOp(ins[:5])

        mem_adr = ins[8:16]

        if op == "jmp":
            ExecuteEngine.flagReset()
            pc = int(mem_adr,2)
            return pc

        elif op == "jlt":
            if fl == "1":
                pc = int(mem_adr,2)
                ExecuteEngine.flagReset()
                return pc
            else:
                pc += 1
                ExecuteEngine.flagReset()
                return pc
            

        elif op == "jgt":
            if fg == "1":
                pc = int(mem_adr,2)
                ExecuteEngine.flagReset()
                return pc
            else:
                pc += 1
                ExecuteEngine.flagReset()
                return pc
            

        elif op == "je":
            if fe == "1":
                pc = int(mem_adr,2)
                ExecuteEngine.flagReset()
                return pc
            else:
                pc += 1
                ExecuteEngine.flagReset()
                return pc
            



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
        return Legend.function[s][0]


main()

x=range(1,len(list)+1)
plt.scatter(x,list)
plt.show()
