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
            elif((line[i-1].isupper() == True and line[i+1].isupper() == True)):
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
    
def DeQuirkify_SestroAlt(line):
    if(line[:6] == "SESTRO"):
        line = line.replace(line[:19], '')
        actual_name = True
    else:
        line = line.replace(line[:16], '')
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

def DeQuirkify_Pozzol(line):
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

def DeQuirkify_Racren(line):
    if(line[:6] == "RACREN"):
        line = line.replace(line[:9], '')
        actual_name = True
    else:
        line = line.replace(line[:5], '')
        actual_name = False
    line = line[:-2]
    if(actual_name):
        line = "RACREN: " + line
    else:
        line = "TR: " + line
    return line

def DeQuirkify_Turnin(line):
    if(line[:6] == "TURNIN"):
        line = line.replace(line[:10], '')
        actual_name = True
    else:
        line = line.replace(line[:6], '')
        actual_name = False
    if(actual_name):
        line = "TURNIN: " + line
    else:
        line = "EI: " + line
    return line
    
def DeQuirkify_Secily(line):
    if(line[:6] == "SECILY"):
        line = line.replace(line[:8], '')
        actual_name = True
    else:
        line = line.replace(line[:4], '')
        actual_name = False
    line = line.split(' ', 1)[1]
    index = line.rfind(' ')
    line = line[:index]
    if(actual_name):
        line = "SECILY: " + line
    else:
        line = "FE: " + line
    return line

def DeQuirkify_Sirage(line):
    if(line[:6] == "SIRAGE"):
        line = line.replace(line[:10], '')
        actual_name = True
    else:
        line = line.replace(line[:6], '')
        actual_name = False
    line = line[:-4]
    line = list(line)
    i = 0
    for c in line:
        if( c == "<"):
            line[i] = "c"
        i+=1
    line = ''.join(line)
    if(actual_name):
        line = "SIRAGE: " + line
    else:
        line = "RM: " + line
    return line

def DeQuirkify_Bytcon(line):
    line = line.replace(line[:12], '')
    line = "BYTCON: " + line
    return line

def DeQuirkify_Husske(line):
    line = line.replace(line[:8], '')
    line = list(line)
    i = 0
    for c in line:
        if (c == "ø"):
            line[i] = "o"
        i+=1
    line = ''.join(line)
    line = "HUSSKE: " + line
    return line

def DeQuirkify_Endari(line):
    line = line.replace(line[:12], '')
    line = line[:-4]
    line = "ENDARI: " + line
    return line

def DeQuirkify_Mshiri(line):
    line = line.replace(line[:8], '')
    line = list(line)
    i = 0
    for c in line:
        if (c == "."):
            line[i] = ""
        i+=1
    line = ''.join(line)
    line = "MSHIRI: " + line
    return line

def DeQuirkify_Raurou(line):
    line = line.replace(line[:8], '')
    line = list(line)
    i = 0
    for c in line:
        if (line[i].isupper() == True):
            line[i] = line[i].lower()
        if (line[i] == '/'):
            if(line[i-1] == " " and line[i+1] == " "):
                line[i] = "I"
            elif(line[i-2] == "?" or line[i-2] == "!" or line[i-2] == "."):
                line[i] = "I"
            else:
                line[i] = "i"
        i+=1
    line[0] = line[0].upper()
    line = ''.join(line)
    line = "RAUROU: " + line
    return line

def DeQuirkify_Sabine(line):
    line = line.replace(line[:14], '')
    line = list(line)
    i = 0
    for c in line:
        if (line[i].isupper() == True):
            line[i] = line[i].lower()
        if (line[i] == 'i'):
            if(line[i-1] == " " and line[i+1] == " "):
                line[i] = "I"
            elif(line[i-2] == "?" or line[i-2] == "!" or line[i-2] == "."):
                line[i] = "I"
            else:
                line[i] = "i"
        i+=1
    line[0] = line[0].upper()
    line = ''.join(line)
    line = "SABINE: " + line
    return line

def DeQuirkify_Necron(line):
    line = line.replace(line[:9], '')
    line = list(line)
    i = 0 
    for c in line:
        if (c == "†"):
            line[i] = ''
        i+=1
    line = ''.join(line)
    line = line.replace(line[:1], ' ')
    line = "NECRON: " + line
    return line

def DeQuirkify_Valtel(line):
    line = line.replace(line[:8], '')
    line = list(line)
    i = 0
    for c in line:
        if(c == "v"):
            if (line[i+1] == "v"):
                line[i] = 'w'
                line[i+1] = ''
            elif(line[i-1] == ' '):
                line[i] = "v"
            elif(line[i-1] + line[i] + line[i+1] + line[i+2] == "ever"):
                line[i] = "v"
            else:
                line[i] = "u"
        i+=1
    line = ''.join(line)
    line = "VALTEL: " + line
    return line

def DeQuirkify_Glomer(line):
    line = line.replace(line[:8], '')
    line = list(line)
    i = 0
    for c in line:
        if (line[i] == "G"):
            line[i] = "g"
        if (line[i] == "M"):
            line[i] = "m"
        i+=1
    line = ''.join(line)
    line = "GLOMER: " + line
    return line

def DeQuirkify_Cinare(line):
    line = line.replace(line[:8], '')
    line = list(line)
    i = 0
    for c in line:
        if (c == "ç"):
            line[i] = "c"
        i+=1
    line = ''.join(line)
    line = "CINARE: " + line
    return line

def DeQuirkify_Crytum(line):
    line = line.replace(line[:11], '')
    line = line[:-3]
    line = "CRYTUM: " + line
    return line

def DeQuirkify_Hayyan(line):
    line = line.replace(line[:8], '')
    line = list(line)
    i = 0
    for c in line:
        if (c == "="):
            line[i] = " "
        elif (c == "⨀"):
            line[i] = "o"
        i+=1
    line = ''.join(line)
    line = "HAYYAN: " + line
    return line

def DeQuirkify_Vilcus(line):
    if(line[:6] == "VILCUS"):
        real_name = True
    else:
        real_name = False
    line = line.replace(line[:29], '')
    line = line[:-22]
    if(real_name):
        line = "VILCUS: " + line
    else:
        line = "ANNOUNCER: " + line
    return line

def DeQuirkify_GuardianSpirit(line):
    line = line.replace(line[:22], '')
    line = line[:-7]
    line = "GUARDIANSPIRIT: " + line
    return line

def DeQuirkify_Executive(line):
    line = line.replace(line[:13], '')
    line = "EXECUTIVE: " + line
    return line

def DeQuirkify_Forgiven(line):
    line = line.replace(line[:14], '')
    line = line[:-5]
    line = "FORGIVEN: " + line 
    return line

def DeQuirkify_Garnie(line):
    line = line[:-3]
    return line

def DeQuirkify_Vellia(line):
    line = line.replace(line[:8], '')
    line = list(line)
    i = 0
    for c in line:
        if(c == "="):
            line[i] = ''
        elif(c == ":"):
            line[i] = ''
        i+=1
    line = ''.join(line)
    line = "VELLIA: " + line
    return line

def DeQuirkify_Neilna(line):
    line = line.replace(line[:9], '')
    line = list(line)
    i = 0
    for c in line:
        if (c == "|"):
            line[i] = " "
        i+=1
    line = ''.join(line)
    line = "NEILNA: " + line
    return line

def DeQuirkify_Keiksi(line):
    line = line.replace(line[:8], '')
    line = list(line)
    i = 0
    for c in line:
        if(c == "@"):
            line[i] = "a"
        i+=1
    line = ''.join(line)
    line = "KEIKSI: " + line
    return line


def DeQuirk(line, page):
    if(line[:2] == "AH" or line[:6] == "ARCJEC" or line[:2] == "AM"):
        newLine = DeQuirkify_Arcjec(line)
    elif(line[:3] == "PO:" or line[:3] == "TAZ"):
        newLine = DeQuirkify_Taz(line)
    elif(line[:2] == "WA" or line[:6] == "LAIVAN"):
        newLine = DeQuirkify_Laivan(line)
    elif(line[:2] == "FF" or line[:6] == "JENTHA"):
        newLine = DeQuirkify_Jentha(line)
    elif(line[:2] == "GD" or line[:6] == "DISMAS"):
        newLine = DeQuirkify_Dismas(line)
    elif(line[:3] == "SA:" or line[:4] == "SOVA"):
        newLine = DeQuirkify_Sova(line)
    elif(line[:2] == "DQ"or line[:6] == "ALBION"):
        newLine = DeQuirkify_Albion(line)
    elif(line[:3] == "ME:" or line[:6] == "OCCEUS"):
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
        if page > 2440:
            newLine = DeQuirkify_SestroAlt(line)
        else:
            newLine = DeQuirkify_Sestro(line)
    elif(line[:6] == "RODERE"):
        newLine = DeQuirkify_Rodere(line)
    elif(line[:2] == "OD" or line[:6] == "HAMIFI"):
        newLine = DeQuirkify_Hamifi(line)
    elif(line[:6] == "POZZOL"):
        newLine = DeQuirkify_Pozzol(line)
    elif(line[:2] == "TR" or line[:6] == "RACREN"):
        newLine = DeQuirkify_Racren(line)
    elif(line[:2] == "EI" or line[:6] == "TURNIN"):
        newLine = DeQuirkify_Turnin(line)
    elif(line[:2] == "FE" or line[:6] == "SECILY"):
        newLine = DeQuirkify_Secily(line)
    elif(line[:2] == "RM" or line[:6] == "SIRAGE"):
        newLine = DeQuirkify_Sirage(line)
    elif(line[:6] == "BYTCON"):
        newLine = DeQuirkify_Bytcon(line)
    elif(line[:6] == "HUSSKE"):
        newLine = DeQuirkify_Husske(line)
    elif(line[:6] == "ENDARI"):
        newLine = DeQuirkify_Endari(line)
    elif(line[:6] == "MSHIRI"):
        newLine = DeQuirkify_Mshiri(line)
    elif(line[:6] == "RAUROU"):
        newLine = DeQuirkify_Raurou(line)
    elif(line[:6] == "SABINE"):
        newLine = DeQuirkify_Sabine(line)
    elif(line[:6] == "NECRON"):
        newLine = DeQuirkify_Necron(line)
    elif(line[:6] == "VALTEL"):
        newLine = DeQuirkify_Valtel(line)
    elif(line[:6] == "GLOMER"):
        newLine = DeQuirkify_Glomer(line)
    elif(line[:6] == "CINARE"):
        newLine = DeQuirkify_Cinare(line)
    elif(line[:6] == "CRYTUM"):
        newLine = DeQuirkify_Crytum(line)
    elif(line[:6] == "HAYYAN"):
        newLine = DeQuirkify_Hayyan(line)
    elif(line[:6] == "VILCUS" or line[:9] == "ANNOUNCER"):
        newLine = DeQuirkify_Vilcus(line)
    elif(line[:14] == "GUARDIANSPIRIT"):
        newLine = DeQuirkify_GuardianSpirit(line)
    elif(line[:9] == "EXECUTIVE"):
        newLine = DeQuirkify_Executive(line)
    elif(line[:8] == "VIVIFIER"):
        newLine = DeQuirkify_Ellsee(line)
        newLine = newLine.replace(newLine[:10], '')
        newLine = "VIVIFIER: " + newLine
    elif(line[:8] == "FORGIVEN"):
        newLine = DeQuirkify_Forgiven(line)
    elif(line[:6] == "GARNIE"):
        newLine = DeQuirkify_Garnie(line)
    elif(line[:6] == "VELLIA"):
        newLine = DeQuirkify_Vellia(line)
    elif(line[:6] == "NEILNA"):
        newLine = DeQuirkify_Neilna(line)
    elif(line[:6] == "KEIKSI"):
        newLine = DeQuirkify_Keiksi(line)
    else:
        newLine = line
    return newLine