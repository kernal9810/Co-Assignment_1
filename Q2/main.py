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

    halt = True
    pc += 1
    type = Legend.getType(ins[:5])
    if type == "A":
        ExecuteEngine.Ex_typeA(ins)
    elif type == "B":
        ExecuteEngine.Ex_typeB(ins)
    elif type == "C":
        ExecuteEngine.Ex_typeC(ins)
    elif type == "D":
        ExecuteEngine.Ex_typeD(ins)
    elif type == "E":
        ExecuteEngine.Ex_typeE(ins)
    elif type == "F":
        ExecuteEngine.Ex_typeF(ins)
    return halt, pc
