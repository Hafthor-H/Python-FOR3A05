#A hluti

def opnaTesla():
    orðabók = {}
    with open("Tesla-1.txt", "r") as skra_inn:
        for line in skra_inn:
            snyrta_linu = line.replace(",", " ").replace(".", " ")
            orðalisti = snyrta_linu.split()
            for orð in orðalisti:
                if orð in orðabók:
                    orðabók[orð] += 1
                else:
                    orðabók[orð] = 1
    print(orðabók)


#C hluti

def openBorge():
    orðabók = {}
    #Opnar texta skrá og snyrtir hana
    with open("Borges-1.txt","r") as skraInn:
        for line in skraInn:
            snyrtaLinu = line.replace(",", " ").replace(".", " ")
            orðalisti = snyrtaLinu.split()
            #Leitar í textaskránni og finur hversu oft hvert orð kemur fyrir. 
            # Gerir tíðnina af orðinu af Key í orðabókinni. Orðin eru Value
            for orð in orðalisti:
                if orð in orðabók:
                    orðabók[orð] += 1
                else:
                    orðabók[orð] = 1
    #.values() gefur okkur Key í orðabókinni
    #.items() gefur okkur Key og Value í orðabókinni
    summaOrða = sum(orðabók.values())

    algengastaOrð = ""
    tiðni_algengasta = 0
    #Fer yfir orðabókina og leitar af algengasta orðinu.
    #Notum tvö variables í for loopinu til að skoða Key og Value í orðabókinni á sama tíma
    for orð, tíðni in orðabók.items():
        if tíðni > tiðni_algengasta:
            algengastaOrð = orð
            tiðni_algengasta = tíðni

    print("Fjöldi orðanna í skránni eru: ", summaOrða)
    print("Algengasta orðið er: ",algengastaOrð)


#D hluti
def openTeslaBorges():
    with open("Borges-1.txt", "r") as opnaBorges, open("Tesla-1.txt", "r") as opnaTesla:
        setBorges = set()
        setTesla = set()
        for lineBorges in opnaBorges:
            snyrtaBorges = lineBorges.replace(", ", " ").replace(". ", " ").replace("\n", " ")
            wordlistBorges = snyrtaBorges.split()
            for wordBorg in wordlistBorges:
                setBorges.add(wordBorg)
                
        for lineTesla in opnaTesla:
            snyrtaTesla = lineTesla.replace(", ", " ").replace(". ", " ").replace("\n", " ")
            wordlistTesla = snyrtaTesla.split()
            for wordTesla in wordlistTesla:
                setTesla.add(wordTesla)

        samengiBorgesOgTesla = setBorges & setTesla
        print("\nHér hefur þú mengið af orðununm í Borges.txt: ", setBorges)
        print("\nHér hefur þú mengið af orðununm í Tesla.txt: ", setTesla)
        print("\nHér hefur þú samengi þeirra tveggja: ", samengiBorgesOgTesla)


       
openTeslaBorges()