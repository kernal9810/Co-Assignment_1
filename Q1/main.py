def A(x,line):
    global error
    global errorName
    global outputList
    str1=''
    if x[0] == 'add':
        str1=str1+'0000000'
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
            elif x[i] == 'FLAGS':
                str1 = str1 + '111'
            else:
                errorName=errorName+'Typo in register name ( LINE ' + str(line) + ')'
                error+=1
    outputList.append(str)

def B(x,line):
    global error
    if x[0] == 'mov':
        print('00010',end='')
    elif x[0] == 'rs':
        print('01000',end='')
    elif x[0] == 'ls':
        print('01001',end='')

    if x[1] == 'R0':
        print('000',end='')
    elif x[1] == 'R1':
        print('001',end='')
    elif x[1] == 'R2':
        print('010',end='')
    elif x[1] == 'R3':
        print('011',end='')
    elif x[1] == 'R4':
        print('100',end='')
    elif x[1] == 'R5':
        print('101',end='')
    elif x[1] == 'R6':
        print('110',end='')
    elif x[1] == 'FLAGS':
        print('111', end='')
    else:
        print('\nTypo in register name ( LINE ',line,')')
        error+=1
        return 0

    if x[2][1:len(x[2])].isdigit():
        value=int(x[2][1:len(x[2])])
        if value>=0 and value<=255:
            print(format(value,'08b'))
        else:
            print('\nIllegal immediate values ( LINE ',line,')')
            error+=1
            return 0
    else:
        print('\nIllegal immediate values ( LINE ',line,')')
        error+=1
        return 0
    return 0

def C(x,line):
    global error
    if x[0] == 'mov':
        print('0001100000',end='')
    elif x[0] == 'div':
        print('0011100000',end='')
    elif x[0] == 'not':
        print('0110100000',end='')
    elif x[0] == 'cmp':
        print('0111000000',end='')

    for i in range(1, 3):
        if i!=2:
            if x[i] == 'R0':
                print('000',end='')
            elif x[i] == 'R1':
                print('001',end='')
            elif x[i] == 'R2':
                print('010',end='')
            elif x[i] == 'R3':
                print('011',end='')
            elif x[i] == 'R4':
                print('100',end='')
            elif x[i] == 'R5':
                print('101',end='')
            elif x[i] == 'R6':
                print('110',end='')
            elif x[i] == 'FLAGS':
                print('111',end='')
            else:
                print('\nTypo in register name ( LINE ',line,')')
                error+=1
                return 0
        else:
            if x[i] == 'R0':
                print('000')
            elif x[i] == 'R1':
                print('001')
            elif x[i] == 'R2':
                print('010')
            elif x[i] == 'R3':
                print('011')
            elif x[i] == 'R4':
                print('100')
            elif x[i] == 'R5':
                print('101')
            elif x[i] == 'R6':
                print('110')
            elif x[i] == 'FLAGS':
                print('111',end='')
            else:
                print('\nTypo in register name ( LINE ',line,')')
                error+=1
                return 0
    return 0

def D(x,line):
    global error
    if x[0] == 'ld':
        print('00100',end='')
    elif x[0] == 'st':
        print('00101',end='')

    if x[1] == 'R0':
        print('000',end='')
    elif x[1] == 'R1':
        print('001',end='')
    elif x[1] == 'R2':
        print('010',end='')
    elif x[1] == 'R3':
        print('011',end='')
    elif x[1] == 'R4':
        print('100',end='')
    elif x[1] == 'R5':
        print('101',end='')
    elif x[1] == 'R6':
        print('110',end='')
    elif x[1] == 'FLAGS':
        print('111', end='')
    else:
        print('\nTypo in register name ( LINE ',line,')')
        error += 1
        return 0

    if x[2] in varmems:
        print(format(varmems[x[2]],'08b'))
    else:
        print('\nUse of undefined variables ( LINE ',line,')')
        error+=1
        return 0
    return 0

def E(x,line):
    global error
    if x[0] == 'jmp':
        print('01111000',end='')
    elif x[0] == 'jlt':
        print('10000000',end='')
    if x[0] == 'jgt':
        print('10001000',end='')
    elif x[0] == 'je':
        print('10010000',end='')

    if x[1] in labmems:
        print(format(labmems[x[1]],'08b'))
    else:
        print('\nUse of undefined labels ( LINE ',line,')')
        error+=1
        return 0
    return 0

error = 0
varmems = {}
labmems = {}

errorName = ''

outputList = []

def main():
    
    global outputList[]
    global errorName
    Input = open("input.txt", "r")

    OutputTxt = open("binaryCompilation.txt", "a")
    
    mems = Input.readlines()
    global error
    i = 0
    v = 0
    totallines = []
    while True:
        line = mems[i]
        totallines.append(line)
        i += 1
        x = line.split()
        if x[0] == 'hlt':
            break
        elif x[0] == 'var':
            v += 1
        elif x[0][len(x[0])-1] ==':':
            temp = x[0][0:len(x[0]) - 1]
            if v!=0:
                labmems[temp] = i - v - 1
            totallines.remove(line)
            tempcount=0
            for ch in line:
                tempcount+=1
                if ch==' ':
                    break
            totallines.append(line[tempcount:len(line)])
    j = 0
    for k in totallines:
        i=k.split()
        if i[0] == 'var':
            varmems[i[1]] = len(totallines) - v + j
            j += 1
    templine=0
    for y in totallines:
        templine+=1
        x=y.split()
        if x[0] == 'var':
            continue
        if x[0] == 'add' or x[0] == 'sub' or x[0] == 'mul' or x[0] == 'xor' or x[0] == 'or' or x[0] == 'and':
            A(x,templine)
            if error!=0:
                break
        elif (x[0] == 'mov' and x[2][0] != 'R') or x[0] == 'rs' or x[0] == 'ls':
            B(x,templine)
            if error!=0:
                break
        elif x[0] == 'mov' or x[0] == 'div' or x[0] == 'not' or x[0] == 'cmp':
            C(x,templine)
            if error!=0:
                break
        elif x[0] == 'ld' or x[0] == 'st':
            D(x,templine)
            if error!=0:
                break
        elif x[0] == 'jmp' or x[0] == 'jlt' or x[0] == 'jgt' or x[0] == 'je':
            E(x,templine)
            if error!=0:
                break
        elif x[0] == 'hlt':
            print('1001100000000000')
        else:
            print('\nTypo in instruction name ( LINE ',templine,')')
            break
            
        if error == 0:
            for i in outputList:
                OutputTxt.write(i)
        else:
            OutputTxt.write(errorName)
                
