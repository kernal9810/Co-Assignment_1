from .BinAsmLegend import Legend
from ExecuteEngine import ExecuteEngine
Mem = open("../TextFiles/BinaryCompilation.txt", "r")

OutputTxt = open("../TextFiles/Output.txt.txt", "a")


def main():

    halt = False
    pc = 0
    while not halt:
        line = Mem.readline()
        if not line:
            break

        halt, new_pc = executeLine(line, pc)

        OutputTxt.write(format(pc, "08b") + " " + Legend.registers["000"] + Legend.registers["001"] + Legend.registers["010"] +
               Legend.registers["011"] + Legend.registers["100"] + Legend.registers["101"] + Legend.registers["110"] +
               Legend.registers["111"] + "\n")



def executeLine(ins, pc):

    halt = False
    pc += 1
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
        pc = ExecuteEngine.Ex_typeD(ins, pc)
    elif type == "E":
        pc = ExecuteEngine.Ex_typeE(ins, pc)
    elif type == "F":
        halt = True
        pc = 0
    return halt, pc
