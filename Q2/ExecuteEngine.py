from BinAsmLegend import Legend


class ExecuteEngine:

    @staticmethod
    def checkOverflow(x):
        flag = Legend.getRegister("111")
        if x > 65535:
            flag = flag[:12] + "1" + flag[13:16]
        else:
            flag = flag[:12] + "0" + flag[13:16]

        Legend.setRegister("111",flag)


    @staticmethod
    def Ex_typeA(ins):
        r = Legend.getRegister(ins[7:10])
        b = int(Legend.getRegister(ins[10:13]))
        c = int(Legend.getRegister(ins[13:16]))

        op = Legend.getOp(ins[:5])

        if   op == "mul":
            Legend.setRegister(r, format(int(b*c,2),"16b"))
            ExecuteEngine.checkOverflow(b*c)

        elif op == "add":
            Legend.setRegister(r,format(int(b + c, 2),"16b"))
            ExecuteEngine.checkOverflow(b+c)

        elif op == "sub":
            Legend.setRegister(r, format(int(b - c, 2), "16b"))
            ExecuteEngine.checkOverflow(b - c)

        elif op == "xor":
            Legend.setRegister(r,format(int(b^c,2),"16b"))

        elif op == "and":
            Legend.setRegister(r, format(int(b and c, 2), "16b"))

        elif op == "or":
            Legend.setRegister(r, format(int(b or c, 2),"16b"))


    @staticmethod
    def Ex_typeB(ins):
        r = Legend.getRegister(ins[5:8])
        b = int(Legend.getRegister(ins[8:16]))

        op = Legend.getOp(ins[:5])
        if op == "mov_im":
            Legend.setRegister(r,format(int(b,2), "16b"))
        elif op == "Lshift":
            Legend.setRegister(r, format(int(b<<1 , 2), "16b"))
        elif op == "Rshift":
            Legend.setRegister(r, format(int(b>>1 , 2), "16b"))


    @staticmethod
    def Ex_typeC(ins):
        r = Legend.getRegister(ins[10:13])
        b = int(Legend.getRegister(ins[13:16]))

        op = Legend.getOp(ins[:5])
        if op == "div":
            q = int(int(r)/b)
            rem = int(r)%b

            Legend.setRegister(Legend.getRegister("000"), format(int(q, 2), "16b"))
            Legend.setRegister(Legend.getRegister("001"), format(int(rem, 2), "16b"))

        elif op == "inv":
            Legend.setRegister(r, format(int(~b, 2), "16b"))

        elif op == "cmp":
            flag = Legend.getRegister("111")
            fl = 0
            fe = 0
            fg = 0

            if int(r) > b:
                fg = 1
            elif int(r) < b:
                fl = 1
            else:
                fe = 1
            flag = flag[:13] + str(fl) + str(fg) + str(fe)

            Legend.setRegister("111", flag)


    # @staticmethod
    # def Ex_typeD(ins):
    #
    #
    # @staticmethod
    # def Ex_typeE(ins):

