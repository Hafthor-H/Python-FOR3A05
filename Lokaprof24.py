def spurning1():
    radius = int(input("Sláðu inn radíus: "))
    val = input("Hvort viltu þú reikna ummál (U), flatarmál (F) eða rúmmál (R) ")

    if val == "F":
        flatarmal = round(radius*radius*3.14,2)
        print(f"Hér hefur þú flatarmálið: {flatarmal}")
    elif val == "U":
        ummal = round(2*radius*3.14,2)
        print(f"Hér hefur þú ummálið: {ummal}")
    elif val == "R":
        rummal = round((4*3.14*radius**3)/3,2)
        print(f"Hér hefur þú rúmmálið: {rummal}")

def spurning2():
    upphaf = int(input("Sláðu inn byrjun á talnabilinu: "))
    endir = int(input("Sláðu inn endan á talnabilinu: "))

    for i in range(upphaf,endir+1):
        if i % 3 == 0 or i % 8 == 0:
            continue
        else:
            print(i)

def spurning3():
    strengur = input("Sláðu inn streng: ")
    Xtala = int(input("Sláðu inn heiltölu: "))
    breytturStrengur = strengur[-3:]
    
    for i in range(Xtala):
        print(breytturStrengur,end="")


#Spurning 4
# 1  1  1  0 1 0
# 64 32 16 8 4 2
# 64+32+16+0+4+0=116

def spurning5():
    orðabók = {}
    with open("JorgeLuisBorgesQuote-1.txt", "r") as skraInn:
        for line in skraInn:
            snyrtaLinu = line.replace(",", " ").replace(".", " ")
            orðalisti = snyrtaLinu.split()
            for orð in orðalisti:
                orð = orð.lower()
                if orð in orðabók:
                    orðabók[orð] += 1
                else:
                    orðabók[orð] = 1
    summaOrða = sum(orðabók.values())

    wordCount = 0
    for key in orðabók.values():
        wordCount += 1

    print("Fjöldi orðanna í skránni eru: ", summaOrða)
    print("Fjöldi ólíkra orða í skránni eru: ", wordCount)

    
def spurning6():
    magnNemanda = int(input("Hvað tóku margir nemedendur þátt í prófinu: "))
    einkunnir = [ ]
    for i in range(magnNemanda):
        einstokEinkunn = int(input("Sláðu inn einkunn: "))
        einkunnir.append(einstokEinkunn)
    

    maxEinkunn = einkunnir[0]
    minEinkunn = einkunnir[0]
    tenCount = 0
    overFive = 0
    overFiveAverage = 0

    for i in einkunnir:
        if i > maxEinkunn:
            maxEinkunn = i

        if i < minEinkunn:
            minEinkunn = i

        if i >= 5:
            overFive += 1
            overFiveAverage += i
        if i == 10:
            tenCount += 1
    
    overFiveAverage = round(overFiveAverage/overFive,2)

    print("Þetta var hæðsta einkunin í bekknunm: ", maxEinkunn)
    print("Þetta var lægðsta einkunin í bekknum: ",minEinkunn)
    print("Svona margir voru með yfir 5 í einkunn: ",overFive)
    print("Þetta er meðaleinkunn þeirra sem voru yfir 5: ",overFiveAverage)
    print("Svona margir voru með 10 í einkunn: ",tenCount)
