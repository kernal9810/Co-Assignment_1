from BinAsmLegend import Legend


class ExecuteEngine:

    @staticmethod
    def checkOverflow(x):
        flag = Legend.getRegister("111")
        if x > 65535:
            flag = flag[:12] + "1" + flag[13:16]
        else:
            flag = flag[:12] + "0" + flag[13:16]

        Legend.setRegister("111", flag)

    @staticmethod
    def Ex_typeA(ins):

        r = ins[7:10]
        b = int(Legend.getRegister(ins[10:13]))
        c = int(Legend.getRegister(ins[13:16]))

        op = Legend.getOp(ins[:5])

        if op == "mul":
            Legend.setRegister(r, format(int(b * c), "16b"))
            ExecuteEngine.checkOverflow(b * c)

        elif op == "add":
            Legend.setRegister(r, format(int(b + c), "16b"))
            ExecuteEngine.checkOverflow(b + c)

        elif op == "sub":
            Legend.setRegister(r, format(int(b - c), "16b"))
            ExecuteEngine.checkOverflow(b - c)

        elif op == "xor":
            Legend.setRegister(r, format(int(b ^ c), "16b"))

        elif op == "and":
            Legend.setRegister(r, format(int(b and c), "16b"))

        elif op == "or":
            Legend.setRegister(r, format(int(b or c), "16b"))

    @staticmethod
    def Ex_typeB(ins):
        r = ins[5:8]
        b = int(Legend.getRegister(ins[8:16]))

        op = Legend.getOp(ins[:5])
        if op == "mov_im":
            Legend.setRegister(r, format(int(b), "16b"))
        elif op == "Lshift":
            Legend.setRegister(r, format(int(b << 1), "16b"))
        elif op == "Rshift":
            Legend.setRegister(r, format(int(b >> 1), "16b"))

    @staticmethod
    def Ex_typeC(ins):
        r = ins[10:13]
        r_1 = Legend.getRegister(r)
        r_2 = Legend.getRegister(ins[13:16])

        b = int(r_2)

        op = Legend.getOp(ins[:5])

        if op == "mov":
            Legend.setRegister(r, r_2)

        elif op == "div":
            q = int(int(r_1) / b)
            rem = int(r_1) % b

            Legend.setRegister("000", format(int(q), "16b"))
            Legend.setRegister("001", format(int(rem), "16b"))

        elif op == "inv":
            Legend.setRegister(r, format(int(~b), "16b"))

        elif op == "cmp":
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
    def Ex_typeD(ins, pc):

        r = ins[5:8]
        op = Legend.getOp(ins[:5])
        address = int(ins[8:])

        if op == "st":
            file = open("../TextFiles/BinaryCompilation.txt", "a")
            r = Legend.getRegister(ins[5:8])


        if op == "ld":
            file = open("../TextFiles/BinaryCompilation.txt", "r")
            mem = file.readlines()
            Legend.setRegister(r, mem[address])


    @staticmethod
    def Ex_typeE(ins, pc):

        flag = Legend.getRegister("111")
        fl = flag[13]
        fg = flag[14]
        fe = flag[15]

        op = Legend.getOp(ins[:5])

        mem_adr = ins[8:16]

        if op == "jmp":
            pc = int(mem_adr)
            return pc

        elif op == "jlt":
            if fl == "1":
                pc = int(mem_adr)
                return pc
            else:
                pc += 1
                return pc

        elif op == "jgt":
            if fg == "1":
                pc = int(mem_adr)
                return pc
            else:
                pc += 1
                return pc

        elif op == "je":
            if fe == "1":
                pc = int(mem_adr)
                return pc
            else:
                pc += 1
                return pc
