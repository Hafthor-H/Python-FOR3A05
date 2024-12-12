#A hluti
def endurskrifa():
    lesa = open("SV1.txt","r" )
    fileInput = lesa.read()
    fileCutOut = fileInput.replace(" ", "").replace("\n", "")
    newFile = open("newFile.txt","w")
    newFile.write(fileCutOut)


def endurskrifaBetra():
    with open("SV1.txt", "r") as skra_inn, open("SV1_lagad.txt", "w") as skra_ut:
        for line in skra_inn:
            snyrt_lina = line.replace(" ", "").replace("\n", "")
            skra_ut.write(snyrt_lina)

#B hluti
def endurSkrifaBhluti():
    with open("SV2.txt", "r") as skra_inn, open("SV2New.txt", "w") as skra_ut:
        for line in skra_inn:
            nöfn = line.split(", ")
            for nafn in nöfn:
                skra_ut.write(nafn.strip() + "\n")
            

#C hluti
def breytaSV2():
    with open("SV2New.txt", encoding="utf-8") as skra_inn, open( "eftirnöfn.txt", "w", encoding="utf-8") as skra_ut:
        for line in skra_inn:
            numer = 1
            nofn = line.split()
            eftirnofn = nofn[-1]
            numer += 1
            skra_ut.write(f"Nemandi númer{numer}: {eftirnofn}" + "\n")

#D hluti
def setningarTxt():
    with open("setningar.txt","w") as skraInn:
        print("\nVelkominnn í ritvél Hafþórs.\nSettu inn eitt orð í einu til að skrifa setningun.\nGerðu '.' til að fá nýja línu og skrifaðu EOF til að loka ritvélinni")
        notandi = ""
        while notandi != "EOF":
            notandi = input("")
            if "." in notandi:
                skraInn.write(notandi + "\n")
            else:
                skraInn.write(notandi + " ")

#E hluti
def opnaOgTelja():
    inputNotanda = input("Sláðu inn nafnið á textaskrá: ")
    with open(inputNotanda + ".txt", "r") as skraInn:
        orðalisti = []
        for line in skraInn:
            lina = line.split()
            for orð in lina:
                if orð not in orðalisti:
                    orðalisti.append(orð)
    lengstaorð = max(orðalisti,key=len)
    print(lengstaorð)
opnaOgTelja()