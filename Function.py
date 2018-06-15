def file1_inlezen():
    #Opent de file en verwijdert de komma's in de attribuut waarde zodat er geen karakters onterecht als scheidingsteken wordt gezien.
    #Returned lijst met daarin alle regels als lijst.
    file = open("Genes_relation.data.txt", "r")
    lines = []
    for line in file.readlines():
        if "CELL GROWTH, CELL DIVISION AND DNA SYNTHESIS" in line:
            line = line.replace('"CELL GROWTH, CELL DIVISION AND DNA SYNTHESIS"', "CELL GROWTH CELL DIVISION AND DNA SYNTHESIS")
        if "CELL RESCUE, DEFENSE, CELL DEATH AND AGEING" in line:
            line = line.replace('"CELL RESCUE, DEFENSE, CELL DEATH AND AGEING"', "CELL RESCUE DEFENSE CELL DEATH AND AGEING")
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

        line = line.strip(".\n").split(",")
        lines.append(line)
    return lines

def file2_inlezen():
    #Leest file in en slaat de data op als een list met daarin van elke regel een lijst van de attribuut waardes.
    file = open("Interactions_relation.data.txt", "r")
    lines = []
    for line in file.readlines():
        line = line.strip(".\n").split(",")
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


def genen_correlatie(genen, inter_lines):
    #Telt het aantal interacties en maakt hier een nieuw attribuut aan. Het voegt dus eigenlijk meerdere attributen samen en maakt hier
    #één nieuw kolom van.
    interaction_dict = {}
    for gen in genen:
        interaction_list = []
        count = physical = genetic = gen_phys = corr = 0
        for line in inter_lines:
            if gen in line:
                count += 1
                if '.' in line[3]:
                    corr += abs(float(line[3]))
                else:
                    avg_corr = None
                if line[2] == 'Genetic':
                    genetic += 1
                elif line[2] == 'Physical':
                    physical += 1
                elif line[2] == 'Genetic-Physical':
                    gen_phys += 1
            else:
                avg_corr = None
        if corr != 0:
            avg_corr = corr / count
            if avg_corr < 0:
                avg_corr = avg_corr
        interaction_list.extend((count, genetic, physical, gen_phys, avg_corr))
        interaction_dict[gen] = interaction_list
    return interaction_dict


def samenvoegen(lines, dict, unieke_genen, int_dict):
    #Verwijderd specifieke attributen en return een list met daarin van elke instantie alle attributen in een list.
    newLines = []
    for gen in unieke_genen:
        for line in lines:
            if gen == line[0]:
                newLine = []
                newLine.append(gen)
                newLine.append(line[1]),
                newLine.append(line[2]),
                newLine.append(line[3]),
                newLine.append(line[4]),
                newLine.append(line[6]),
                for boolean in dict[gen]:
                    newLine.append(str(boolean))
                newLine.append(line[8])
                for val in int_dict[gen]:
                    newLine.append(str(val))
                newLines.append(newLine)
    return newLines


def wegschrijven(lines):
    #Maakt een nieuwe file aan en schrijft van elke instantie alle attributen weg.
    new_file = open('genes_interactions_relations.txt', 'w')
    uniq = []
    new_file.write(
        "genID,essential,class,complex,phenotype,chromosome,CELL GROWTH CELL DIVISION AND DNA SYNTHESIS,CELL RESCUE DEFENSE CELL DEATH AND AGEING,CELLULAR BIOGENESIS,CELLULAR COMMUNICATION/SIGNAL TRANSDUCTION,CELLULAR ORGANIZATION,CELLULAR TRANSPORT AND TRANSPORTMECHANISMS,ENERGY,IONIC HOMEOSTASIS,METABOLISM,PROTEIN DESTINATION,PROTEIN SYNTHESIS,TRANSCRIPTION,TRANSPORT FACILITATION,localization,aantal_correlaties,genetic,physical,genetic-physical,gem_correlatie\n")
    for line in lines:
        if line[0] not in uniq:
            new_file.write(','.join(line) + '\n')
            uniq.append(line[0])
    new_file.close()


def main():
    functies = ["CELL GROWTH CELL DIVISION AND DNA SYNTHESIS", "CELL RESCUE DEFENSE CELL DEATH AND AGEING",
                "CELLULAR BIOGENESIS (proteins are not localized to the corresponding organelle)",
                "CELLULAR COMMUNICATION/SIGNAL TRANSDUCTION",
                "CELLULAR ORGANIZATION (proteins are localized to the corresponding organelle)",
                "CELLULAR TRANSPORT AND TRANSPORTMECHANISMS", "ENERGY", "IONIC HOMEOSTASIS", "METABOLISM",
                "PROTEIN DESTINATION", "PROTEIN SYNTHESIS", "TRANSCRIPTION", "TRANSPORT FACILITATION"]
    lines = file1_inlezen()

    unieke_genen = genen_zoeken(lines)
    gen_function_dict = functiecode_maken(unieke_genen, lines, functies)
    interaction_lines = file2_inlezen()

    uniq_interaction = []
    for i in interaction_lines:
        if i[0] not in uniq_interaction:
            uniq_interaction.append(i[0])
        if i[1] not in uniq_interaction:
            uniq_interaction.append(i[1])

    sort_lines = sorted(interaction_lines)
    interaction_dict = genen_correlatie(unieke_genen, sort_lines)

    newLines = samenvoegen(lines, gen_function_dict, unieke_genen, interaction_dict)
    newLines = [list(x) for x in set(tuple(x) for x in newLines)]

    wegschrijven(newLines)


main()
