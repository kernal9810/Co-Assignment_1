import sys


def regcheck(x, str2, line, i):
    global errorName
    global error
    if x[i] == 'R0':
        str2 = str2 + '000'
    elif x[i] == 'R1':
        str2 = str2 + '001'
    elif x[i] == 'R2':
        str2 = str2 + '010'
    elif x[i] == 'R3':
        str2 = str2 + '011'
    elif x[i] == 'R4':
        str2 = str2 + '100'
    elif x[i] == 'R5':
        str2 = str2 + '101'
    elif x[i] == 'R6':
        str2 = str2 + '110'
    elif x[i] == 'FLAGS' or x[i] == 'R7':
        errorName = 'Illegal use of FLAGS ( LINE ' + str(line) + ')'
        error += 1
    else:
        errorName = 'Typo in register name ( LINE ' + str(line) + ')'
        error += 1
    return str2


def A(x, line):
    global error
    global errorName
    global outputList
    str1 = ''
    if x[0] == 'add':
        str1 = str1 + '0000000'
    elif x[0] == 'sub':
        str1 = str1 + '0000100'
    elif x[0] == 'mul':
        str1 = str1 + '0011000'
    elif x[0] == 'xor':
        str1 = str1 + '0101000'
    elif x[0] == 'or':
        str1 = str1 + '0101100'
    elif x[0] == 'and':
        str1 = str1 + '0110000'

    for i in range(1, 4):
        if error == 0:
            str1 = regcheck(x, str1, line, i)

    outputList.append(str1)


def B(x, line):
    global error
    global errorName
    global outputList
    str1 = ''
    if x[0] == 'mov':
        str1 = str1 + '00010'
    elif x[0] == 'rs':
        str1 = str1 + '01000'
    elif x[0] == 'ls':
        str1 = str1 + '01001'

    str1 = regcheck(x, str1, line, 1)

    if error == 0 and x[2][1:len(x[2])].isdigit():
        value = int(x[2][1:len(x[2])])
        if value >= 0 and value <= 255:
            str1 = str1 + format(value, '08b')
        else:
            errorName = 'Illegal immediate values ( LINE ' + str(line) + ')'
            error += 1
    else:
        errorName = 'Illegal immediate values ( LINE ' + str(line) + ')'
        error += 1
    outputList.append(str1)


def C(x, line):
    global error
    global errorName
    global outputList
    str1 = ''
    if x[0] == 'mov':
        str1 = str1 + '0001100000'
    elif x[0] == 'div':
        str1 = str1 + '0011100000'
    elif x[0] == 'not':
        str1 = str1 + '0110100000'
    elif x[0] == 'cmp':
        str1 = str1 + '0111000000'

    for i in range(1, 3):
        if error == 0:
            if x[i] == 'R0':
                str1 = str1 + '000'
            elif x[i] == 'R1':
                str1 = str1 + '001'
            elif x[i] == 'R2':
                str1 = str1 + '010'
            elif x[i] == 'R3':
                str1 = str1 + '011'
            elif x[i] == 'R4':
                str1 = str1 + '100'
            elif x[i] == 'R5':
                str1 = str1 + '101'
            elif x[i] == 'R6':
                str1 = str1 + '110'
            elif x[0] == 'mov' and i == 2 and (x[i] == 'FLAGS' or x[i] == 'R7'):
                str1 = str1 + '111'
            elif x[i] == 'FLAGS' or x[i] == 'R7':
                errorName = 'Illegal use of FLAGS ( LINE ' + str(line) + ')'
                error += 1
            else:
                errorName = 'Typo in register name ( LINE ' + str(line) + ')'
                error += 1
    outputList.append(str1)


def D(x, line):
    global error
    global errorName
    global outputList
    global labmems
    global varmems
    str1 = ''
    if x[0] == 'ld':
        str1 = str1 + '00100'
    elif x[0] == 'st':
        str1 = str1 + '00101'

    str1 = regcheck(x, str1, line, 1)

    if x[2] in labmems:
        errorName = 'Label used instead of variable ( LINE ' + str(line) + ')'
        error += 1
    if error == 0:
        if x[2] in varmems:
            str1 = str1 + format(varmems[x[2]], '08b')
        else:
            errorName = 'Use of undefined variables ( LINE ' + str(line) + ')'
            error += 1
    outputList.append(str1)


def E(x, line):
    global error
    global errorName
    global outputList
    global varmems
    global labmems
    str1 = ''
    if x[0] == 'jmp':
        str1 = str1 + '01111000'
    elif x[0] == 'jlt':
        str1 = str1 + '10000000'
    if x[0] == 'jgt':
        str1 = str1 + '10001000'
    elif x[0] == 'je':
        str1 = str1 + '10010000'

    if x[1] in varmems:
        errorName = 'Variable used instead of label ( LINE ' + str(line) + ')'
        error += 1
    if error == 0:
        if x[1] in labmems:
            str1 = str1 + format(labmems[x[1]], '08b')
        else:
            errorName = 'Use of undefined labels ( LINE ' + str(line) + ')'
            error += 1
    outputList.append(str1)


error = 0
varmems = {}
labmems = {}
errorName = ''
outputList = []


def main():
    global outputList
    global errorName
    global error

    complete_input = sys.stdin.read()
    mems = (complete_input.split("\n"))
    # file = open('Input.txt', 'r')
    # mems = file.readlines()
    pc = 0
    emptylines = 0
    v = 0
    totallines = []

    totalEmptylines = 0
    for i in mems:
        if len(i) == 0:
            totalEmptylines += 1

    while pc < len(mems):

        line = mems[pc]
        pc += 1
        totallines.append(line)
        lineWithoutLabel = 'lineWithoutLabel'
        if len(line) > 1:
            x = line.split()

            if x[0][len(x[0]) - 1] == ':':
                temp = x[0][0:len(x[0]) - 1]
                labmems[temp] = pc - emptylines - v - 1
                totallines.remove(line)
                tempcount = 0
                for ch in line:
                    tempcount += 1
                    if ch == ' ':
                        break
                lineWithoutLabel = line[tempcount:len(line)]
                totallines.append(lineWithoutLabel)
                x = lineWithoutLabel.split()
                if len(lineWithoutLabel) == 0:
                    totalEmptylines += 1
                    emptylines += 1

            if len(lineWithoutLabel) > 1:
                if ('hlt' in x) and pc != len(mems) - (totalEmptylines - emptylines):
                    errorName = 'Illegal use of hlt ( LINE ' + str(pc) + ')'
                    error += 1
                elif (pc == len(mems) - (totalEmptylines - emptylines)) and x[0] == 'hlt':
                    break
                elif (pc == len(mems) - (totalEmptylines - emptylines)) and x[0] != 'hlt':
                    errorName = 'hlt absent'
                    error += 1
                if x[0] == 'var':
                    if (pc - v - emptylines) == 1:
                        v += 1
                    else:
                        error += 1
                        errorName = 'VAR not initialized at start of instructions ( Line ' + str(pc) + ')'
        else:
            emptylines += 1

        j = 0
        for k in totallines:
            if len(k) > 4:
                i = k.split()
                if i[0] == 'var':
                    varmems[i[1]] = len(totallines) - v + j - emptylines + 1
                    j += 1
    checkwhich(totallines, emptylines)
    # file.close()


def checkwhich(list1, emptylines):
    global error
    global errorName
    global outputList
    # outputTxt = open('binaryCompilation.txt', 'w')
    templine = emptylines
    if error == 0:
        for y in list1:
            if len(y) <= 1:
                continue
            else:
                if error == 0:
                    templine += 1
                    x = y.split()
                    if x[0] == 'var':
                        continue
                    if x[0] == 'add' or x[0] == 'sub' or x[0] == 'mul' or x[0] == 'xor' or x[0] == 'or' or x[
                        0] == 'and':
                        if len(x) == 4:
                            A(x, templine)
                        else:
                            errorName = 'Syntax error for Type A ( Line ' + str(templine) + ')'
                            error += 1
                    elif (x[0] == 'mov' and (len(x) < 3 or (x[2][0] != 'R' and x[2][0] != 'F'))) or x[0] == 'rs' or x[
                        0] == 'ls':
                        if len(x) == 3:
                            B(x, templine)
                        else:
                            errorName = 'Syntax error for Type B ( Line ' + str(templine) + ')'
                            error += 1
                    elif x[0] == 'mov' or x[0] == 'div' or x[0] == 'not' or x[0] == 'cmp':
                        if len(x) == 3:
                            C(x, templine)
                        else:
                            errorName = 'Syntax error for Type C ( Line ' + str(templine) + ')'
                            error += 1
                    elif x[0] == 'ld' or x[0] == 'st':
                        if len(x) == 3:
                            D(x, templine)
                        else:
                            errorName = 'Syntax error for Type D ( Line ' + str(templine) + ')'
                            error += 1
                    elif x[0] == 'jmp' or x[0] == 'jlt' or x[0] == 'jgt' or x[0] == 'je':
                        if len(x) == 2:
                            E(x, templine)
                        else:
                            errorName = 'Syntax error for Type E ( Line ' + str(templine) + ')'
                            error += 1
                    elif x[0] == 'hlt':
                        outputList.append('1001100000000000')
                    else:
                        errorName = 'Typo in instruction name ( LINE ' + str(templine) + ')'
                        outputList.append(errorName)
                        error += 1
                else:
                    break
    if error == 0:
        for i in outputList:
            print(i)
            # outputTxt.write(str(i) + "\n")
    else:
        print(errorName)
        # outputTxt.write(errorName)
    # outputTxt.close()


main()