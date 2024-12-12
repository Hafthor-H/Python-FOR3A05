def höfudborgir():
    borgir =  ["Róm", "Washington", "Reykjavík", "París", "Kaupmannahöfn"]
    userInput = input("Sláðu inn höfuðborg: ")
    #Leitar í listanum til að gá hvort borgin sé til
    if userInput in borgir:
        print(userInput, "er núþegar í listanum \n")
        print(borgir)
    else:
        #Bætir orðinu við ef það finnst ekki í listanum
        baetaVid = input("Borgin fannst ekki í listanum, má bjóða þér að bæta henni við? Y/N: ")
        if baetaVid == "Y":
            borgir.append(userInput)
            print("Hér er listinn ásamt borginni sem þú bættir við \n",borgir)
        else:
            print("Ein leiðinlegt en hér er amk listin af borgunum: ")
            print(borgir)

def einkunnir():
    einkunnirListi = []
    magnNemanda = int(input("Hveru margir nemendur tóku prófið: "))
    #Setur tölur inn í tómalistann fyrir magnNemanda 
    for i in range(magnNemanda):
        einkunnirTölur = int(input("Einkunn: "))
        einkunnirListi.append(einkunnirTölur)
    
    #Geri max að fyrstu töluni í listanum og geng svo yfir listan til að finna stærri tölu
    max = einkunnirListi[0]
    for i in einkunnirListi:
        if i > max: 
            max = i
        else:
            continue
    #Geri min að fyrstu töluni í listanum og geng svo yfir listan til að finna minni tölu
    min = einkunnirListi[0]
    for j in einkunnirListi:
        if j < min:
            min = j
        else:
            continue
    #Legg saman einkunirnar og deili því með magnNemanda
    average = 0
    for h in einkunnirListi:
        average += h

    average = average / magnNemanda

    #Tel hversu margir voru með 5 eða yfir
    fiveCounter = 0
    for k in einkunnirListi:
        if k >= 5:
            fiveCounter += 1
        else:
            continue

    #Prenta niðurstöður :)
    print("Þetta er listinni: ",einkunnirListi)
    print("Þetta er hæðsta einkunnin: ", max)
    print("Þetta er lægsta einkunnin: ", min)
    print("Þetta er meðal einkunnin: ", average)
    print("Svona margir voru með 5 eða yfir: ", fiveCounter)


def borges():
    #Geri tóma orðabók og opna borges
    orðabok = {}
    with open("borgesTilvitnun.txt","r", encoding="utf-8") as skraInn:
        #Setjum borges í klippingu og gerum textan fínan
        for line in skraInn:
            snyrtaLinu = line.replace(",", " ").replace(".", " ")
            orðalisti = snyrtaLinu.split()
            #Setjum orðin í borges inn í tómu orðabókina og teljum hversu oft orðin komu fram
            for orð in orðalisti:
                if orð in orðabok:
                    orðabok[orð] += 1
                else:
                    orðabok[orð] = 1
            #Finnum hversu mörg orðin eru 
            summaOrða = sum(orðabok.values())

    algengastaOrð = ""
    tiðni_algengasta = 0
    #Fer yfir orðabókina og leitar af algengasta orðinu.
    #Notum tvö variables í for loopinu til að skoða Key og Value í orðabókinni á sama tíma
    for orð, tíðni in orðabok.items():
        if tíðni > tiðni_algengasta:
            algengastaOrð = orð
            tiðni_algengasta = tíðni
    #Teljum einstöku orðin með því að telja lyklana
    uniqueWord = 0
    for i in orðabok:
        uniqueWord += 1
    
    print("Fjöldi orðanna í skránni eru: ", summaOrða)
    print("Fjöldi ólíkra orða í skránni eru: ",uniqueWord)
    print("Algengasta orðið er: ",algengastaOrð)