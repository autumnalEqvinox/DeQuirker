def deSlashify(newLine):
    newLine = list(newLine)
    i = 0
    for c in newLine:
        if (newLine[i]== "\\"):
            newLine[i] = ''
        i+=1
    newLine = ''.join(newLine)
    return newLine

def DeQuirkify_Arcjec(line):
    if(line[:6] == "ARCJEC"):
        line = line.replace(line[:13], '')
        actual_name = True
    else:
        line = line.replace(line[:9], '')
        actual_name = False
    line = line[:-5]
    if(actual_name):
        line = "ARCJEC: " + line
    else:
        line = "AH: " + line
    return line 

def DeQuirkify_Taz(line):
    if(line[:3] == "TAZ"):
        line = line.replace(line[:6], '')
        actual_name = True
    else:
        line = line.replace(line[:5], '')
        actual_name = False
    line = line[:-2]
    i = 0
    line = list(line)
    line.append('')
    for c in line:
        if (c == "+"):
            if(line[i-1].isupper() == True or line[i+1].isupper() == True):
                line[i] = "T"
            else:
                line[i] = "t"
        i+=1
    line = ''.join(line)
    if(actual_name):
        line = "TAZ: " + line
    else: 
        line = "PO: " + line
    return line

def DeQuirkify_Laivan(line):
    return line

def DeQuirkify_Jentha(line):
    linenew = ""
    linewords = line.split(" ") 
    for i in range(len(linewords)):
        if len(linewords[i]) > 1 or (linewords[i] in ["a", "i"] and linewords[i] != linewords[i+1][0]):
            linenew += linewords[i] + " "
    if len(linewords) == 3 and len(linewords[2]) == 1:
        linenew += linewords[2]
    line = linenew
    return line

def DeQuirkify_Dismas(line):
    if(line[:6] == "DISMAS"):
        line = line.replace(line[:8], '')
        actual_name = True
    else:
        line = line.replace(line[:4], '')
        actual_name = False
    line = line[:-4]
    line = list(line)
    line.append('')
    line.append('')
    i = 0
    for c in line:
        if (line[i-1] + line[i] == "/\\"):
                line[i-1] = "a"
                line[i] = ''
        elif ((line[i-1] + line[i] == "\\/")):
                line[i-1] = "v"
                line[i] = ''
        i+=1
    line = ''.join(line)
    if(actual_name):
        line = "DISMAS: " + line
    else:
        line = "GD: " + line
    return line

def DeQuirkify_Sova(line):
    if(line[:4] == "SOVA"):
        line = line.replace(line[:6], '')
        actual_name = True
    else:
        line = line.replace(line[:5], '')
        actual_name = False
    line = line[:-2]
    if(actual_name):
        line = "SOVA: "
    else:
        line = "SA: " + line
    return line

def DeQuirkify_Albion(line):
    if(line[:6] == "ALBION"):
        line = line.replace(line[:9], '')
        actual_name = True
    else:
        line = line.replace(line[:5], '')
        actual_name = False
    line = list(line)
    i = 0
    for c in line:
        if (c == "*"):
            line[i] = " "
        if(c == "!" or c == "?" or c == "." and line[i-1] == " "):
            line[i-1] = c
            line[i] = ''
        i+=1
    line = ''.join(line)
    if(actual_name):
        line= "ALBION: " + line
    else:
        line = "DQ: " + line
    return line

def DeQuirkify_Occeus(line):
    if(line[:6] == "OCCEUS"):
        line = line.replace(line[:8], '')
        actual_name = True
    else:
        line = line.replace(line[:4], '')
        actual_name = False
    line = list(line)
    i = 0
    for c in line:
        if (line[i-2] + line[i-1] + line[i] == ".o."):
            line[i] = ""
            line[i-1] = ""
            line[i-2] = "o"
        elif((line[i-3] + line[i-2] + line[i-1] + line[i] == ".oo.")):
            line[i] = ""
            line[i-1] = ""
            line[i-2] = ""
            line[i-3] = "oo"
        elif (line[i-2] + line[i-1] + line[i] == "eye" or line[i-2] + line[i-1] + line[i] == "Eye" ):
            line[i-2] = "I"
            line[i-1] = ""
            line[i] = ""
        i+=1
    line = ''.join(line)
    if(actual_name):
        line = "OCCEUS: " + line
    else:
        line = "ME: " + line
    return line

def DeQuirkify_Serpaz(line):
    return line

def DeQuirkify_Murrit(line):
    if(line[:6] == "MURRIT"):
        line = line.replace(line[:11], '')
        actual_name = True
        BOOB = False
    elif (line[:9] == "BOOBDRONE"):
        line = line.replace(line[:14], '')
        actual_name = True
        BOOB = True
    else:
        line = line.replace(line[:7], '')
        actual_name = False
    line = line[:-2]
    line = list(line)
    i = 0
    for c in line:
        if (c == "#"):
            line[i] = "h"
        i+=1
    line = ''.join(line)
    if(actual_name):
        if(BOOB != True):
            line = "MURRIT: " + line
        else:
            line = "BOOBDRONE: " + line
    else:
        line = "UK: " + line
    line = deSlashify(line)
    return line

def DeQuirkify_Calder(line):
    return line

def DeQuirkify_Ellsee(line):
    if(line[:6] == "ELLSEE"):
        line = line.replace(line[:8], '')
        actual_name = True
    else:
        line = line.replace(line[:4], '')
        actual_name = False
    test_list = list(line)
    i = 0
    for c in test_list:
        if (c == "Σ"):
            if(line[i-1] == line[0] and line[i+1].isupper() != True):
                test_list[i] = "e"
            elif((line[i-1].isupper() == True or line[i+1].isupper() == True)):
                test_list[i] = "E"
            elif(line[i] == line[0]):
                test_list[i] = "E"
            else:
                test_list[i] = "e"
        elif (c == "¡"):
            test_list[i] = "!"
        elif (c == "¿"):
            test_list[i] = "?"
        i+=1
    line = deSlashify(line)
    line = ''.join(test_list)
    if(actual_name):
        line = "ELLSEE: " + line
    else:
        line = "EO: " + line
    return line

def DeQuirkify_Sestro(line):
    if(line[:6] == "SESTRO"):
        line = line.replace(line[:9], '')
        actual_name = True
    else:
        line = line.replace(line[:5], '')
        actual_name = False
    if(actual_name):
        line = "SESTRO: " + line
    else:
        line = "CF: " + line
    return line

def DeQuirkify_Hamifi(line):
    if(line[:6] == "HAMIFI"):
        line = line.replace(line[:8], '')
        actual_name = True
    else:
        line = line.replace(line[:4], '')
        actual_name = False
    line = line[:-2]
    if(actual_name):
        line = "HAMIFI: " + line
    else:
        line = "OD: " + line
    return line

def DeQuirkify_Rodere(line):
    line = line.replace(line[:9], '')
    line = line[:-3]
    line = list(line)
    i = 0
    for c in line:
        if (c == "-"):
            line[i] = " "
        i+=1
    line = ''.join(line)
    line = "RODERE: " + line
    return line

def Dequirkify_Pozzol(line):
    line = line.replace(line[:8], '')
    line = list(line)
    i = 0
    for c in line:
        if (line[i].isupper() == True):
            line[i] = line[i].lower()
        i+=1
    line[0] = line[0].upper()
    line = ''.join(line)
    line = "POZZOL: " + line
    return line
    



def DeQuirk(line):
    if(line[:2] == "AH" or line[:6] == "ARCJEC"):
        newLine = DeQuirkify_Arcjec(line)
    elif(line[:3] == "PO:" or line[:3] == "TAZ"):
        newLine = DeQuirkify_Taz(line)
    elif(line[:2] == "WA" or line[:6] == "LAIVAN"):
        newLine = DeQuirkify_Laivan(line)
    elif(line[:2] == "FF" or line[:6] == "JENTHA"):
        newLine = DeQuirkify_Jentha(line)
    elif(line[:2] == "GD" or line[:6] == "DISMAS"):
        newLine = DeQuirkify_Dismas(line)
    elif(line[:2] == "SA" or line[:4] == "SOVA"):
        newLine = DeQuirkify_Sova(line)
    elif(line[:2] == "DQ"or line[:6] == "ALBION"):
        newLine = DeQuirkify_Albion(line)
    elif(line[:2] == "ME" or line[:6] == "OCCEUS"):
        newLine = DeQuirkify_Occeus(line)
    elif(line[:2] == "PD" or line[:6] == "SERPAZ"):
        newLine = DeQuirkify_Serpaz(line)
    elif(line[:2] == "UK" or line[:6] == "MURRIT" or line[:9] == "BOOBDRONE"):
        newLine = DeQuirkify_Murrit(line)
    elif(line[:2] == "GS" or line[:6] == "CALDER"):
        newLine = DeQuirkify_Calder(line)
    elif(line[:2] == "EO" or line[:6] == "ELLSEE"):
        newLine = DeQuirkify_Ellsee(line)
    elif(line[:2] == "CF" or line [:6] == "SESTRO"):
        newLine = DeQuirkify_Sestro(line)
    elif(line[:6] == "RODERE"):
        newLine = DeQuirkify_Rodere(line)
    elif(line[:2] == "OD" or line[:6] == "HAMIFI"):
        newLine = DeQuirkify_Hamifi(line)
    elif(line[:6] == "POZZOL"):
        newLine = Dequirkify_Pozzol(line)
    else:
        newLine = line
    return newLine