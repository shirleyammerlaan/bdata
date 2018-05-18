


def file_inlezen():
    #Returned lijst met daarin alle regels als lijst.
    file = open("Genes_relation.data.txt", "r")
    lines = []
    for line in file.readlines():
        if "CELL GROWTH, CELL DIVISION AND DNA SYNTHESIS" in line:
            line = line.replace("CELL GROWTH, CELL DIVISION AND DNA SYNTHESIS", "CELL GROWTH CELL DIVISION AND DNA SYNTHESIS")
        if "CELL RESCUE, DEFENSE, CELL DEATH AND AGEING" in line:
            line = line.replace("CELL RESCUE, DEFENSE, CELL DEATH AND AGEING", "CELL RESCUE DEFENSE CELL DEATH AND AGEING")
        if "Auxotrophies, carbon and" in line:
            line = line.replace("Auxotrophies, carbon and", "Auxotrophies carbon and")
        if "Fatty acid synthetase, cytoplasmic" in line:
            line = line.replace("Fatty acid synthetase, cytoplasmic", "Fatty acid synthetase cytoplasmic")
        if "Endonuclease SceI, mitochondrial" in line:
            line = line.replace("Endonuclease SceI, mitochondrial","Endonuclease SceI mitochondrial")
        if "H+-transporting ATPase, vacuolar" in line:
            line = line.replace("H+-transporting ATPase, vacuolar","H+-transporting ATPase vacuolar")
        if "Alpha, alpha-trehalose-phosphate synthase" in line:
            line = line.replace("Alpha, alpha-trehalose-phosphate synthase","Alpha alpha-trehalose-phosphate synthase")
        if "Proteases, mitochondrial" in line:
            line = line.replace("Proteases, mitochondrial","Proteases mitochondrial")
        if "Auxotrophies, carbon and" in line:
            line = line.replace("Auxotrophies, carbon and","Auxotrophies carbon and")

        line = line.split(",")
        lines.append(line)
    return lines

def genen_zoeken(lines):
    #Zet alle genen die er zijn in een lijst en returned dit, dus geen dubbele genen hier.
    genen = []
    for line in lines:
        if line[0] not in genen:
            genen.append(line[0])
    return genen

def functiecode_maken(genen, lines, alle_functies):
    #Maakt per gen een lijst met alle functies die het geen heeft, dit zet die in een dict met de gennaam.
    #Vervolgens wordt de in de dictTF als key gennaam en als value list met True en False gemaakt.
    dictFun = {}
    for gen in genen:
        list_function = []
        for line in lines:
            if line[0] == gen:
                list_function.append(line[7])
        dictFun[gen] = list_function

    dictTF = {}
    for gen in dictFun:
        listTF = []
        for functie in alle_functies:
            if functie in dictFun[gen]:
                listTF.append(True)
            else:
                listTF.append(False)
        dictTF[gen] = listTF
    return(dictTF)

def samenvoegen(lines, dict):
    


def main():
    functies = ["CELL GROWTH CELL DIVISION AND DNA SYNTHESIS", "CELL RESCUE DEFENSE CELL DEATH AND AGEING",
                "CELLULAR BIOGENESIS (proteins are not localized to the corresponding organelle)",
                "CELLULAR COMMUNICATION/SIGNAL TRANSDUCTION",
                "CELLULAR ORGANIZATION (proteins are localized to the corresponding organelle)",
                "CELLULAR TRANSPORT AND TRANSPORTMECHANISMS", "ENERGY", "IONIC HOMEOSTASIS", "METABOLISM",
                "PROTEIN DESTINATION", "PROTEIN SYNTHESIS", "TRANSCRIPTION", "TRANSPORT FACILITATION",
                "TRANSPOSABLE ELEMENTS VIRAL AND PLASMID PROTEINS"]
    lines = file_inlezen()
    unieke_genen = genen_zoeken(lines)
    gen_function_dict = functiecode_maken(unieke_genen,lines,functies)





    #Om zelfde genen bij elkaar te laten staan maar dit staan ze al
    for gen in unieke_genen:
        for line in lines:
            if line[0] == gen:
                pass







main()