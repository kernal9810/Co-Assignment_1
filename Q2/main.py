from .BinAsmLegend import Legend

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
    Legend.getType(ins[:5])

    return halt, pc
