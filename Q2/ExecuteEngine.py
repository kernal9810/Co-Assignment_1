from BinAsmLegend import Legend

class ExecuteEngine:
    def Ex_typeA(self,ins):
        r = Legend.getRegister(ins[7:10])
        b = int(Legend.getRegister(ins[10:13]))
        c = int(Legend.getRegister(ins[13:16]))

        op = Legend.getOp(ins[:5])

        if   op == "mul":
            Legend.setRegister(r, format(int(b*c,2),"16b"))
        elif op == "add":
            Legend.setRegister(r,format(int(b + c, 2),"16b"))
        elif op == "sub":
            Legend.setRegister(r, format(int(b - c, 2), "16b"))
        elif op == "xor":
            Legend.setRegister(r,format(int(b^c,2),"16b"))
        elif op == "and":
            Legend.setRegister(r, format(int(b and c, 2), "16b"))
        elif op == "or":
            Legend.setRegister(r, format(int(b or c, 2),"16b"))

    def Ex_typeB(self,ins):
        r = Legend.getRegister(ins[5:8])
        b = int(Legend.getRegister(ins[8:16]))

        op = Legend.getOp(ins[:5])
        if op == "mov_im":
            Legend.setRegister(r,format(int(b,2), "16b"))
        elif op == "Lshift":
            Legend.setRegister(r, format(int(b<<1 , 2), "16b"))
        elif op == "Rshift":
            Legend.setRegister(r, format(int(b>>1 , 2), "16b"))


    def Ex_typeC(self,ins):
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
            
    def Ex_typeD:
    def Ex_typeE:
    def Ex_typeF: