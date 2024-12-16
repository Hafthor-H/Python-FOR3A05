def spurning1():
    artal = int(input("Sláðu inn ártal: "))
    if artal % 1000 == 0:
        print(f"árið {artal} byrjaði ný árþúsund!")
    elif artal % 100 == 0:
        print(f"árið {artal} byrjaði ný öld!")
    elif artal == 1964:
        print(f"Árið {artal} var HR stofnað ")
    else:
        print(f"Það er ekki áhugavert við árið {artal} :( ")

def spurning2():
    upphaf = int(input("Sláðu inn upphaf talnabils: "))
    endir = int(input("Sláðu inn endi talnabils: "))

    val = input("Hvort vilt þú talnabilið í réttri (R) röð eða öfugri röð? (Ö): ")
    
    if val == "R":
        for i in range(upphaf,endir):
            if i % 3 == 0 or i % 5 == 0:
                continue
            else:
                print(i)

    elif val == "Ö":
        for i in range(endir, upphaf-1,-1):
            if i % 3 == 0 or i % 5 == 0:
                continue
            else:
                print(i)

# Spurning 3 

# 1  1  0   1  0  1 
# 32 16 8  4  2  1 
# 32+16+4+1= 53

def spurning4():
    strengur = str(input("Sláðu inn streng: "))
    x = int(input("Sláðu inn heiltölu: "))

    val = input("Viltu sjá strengin í réttri röð(R) eða öfugri röð(Ö)")

    if val == "R":
        print(strengur[::x])
    elif val == "Ö":
        print(strengur[::-x])

def flatarmalHrings(radius):
    return radius*radius*3.14

def rummalHrings(radius):
    return (4*3.14*radius**3)/3

def spurning5():
    radius = int(input("Sláðu inn radíus: "))
    val = input("Viltu reikna flatarmál (F) eða rúmmál (R) ")

    if val == "R":
        print(round(rummalHrings(radius),2))
    if val == "F":
        print(round(flatarmalHrings(radius),2))

class kula:
    def __init__(self,radius):
        self.radius = radius 

    def __str__(self):
        return f"Radíusinn er: {self.radius}"
    
    def rummalHrings(self):
        return round((4*3.14*self.radius**3)/3,2)
    

def spurning6():
    radius = int(input("Sláðu inn radíus kúlu: "))
    kulann = kula(radius)
    print(kulann)
    print("Rúmmal kúlunnar er: ",kulann.rummalHrings())


def spurning7():
    orðabók = {}
    with open("HanSolo.txt", "r") as skraInn:
        for line in skraInn:
            snyrtaLinu = line.replace(",", " ").replace(".", " ")
            orðalisti = snyrtaLinu.split()
            for orð in orðalisti:
                if orð in orðabók:
                    orðabók[orð] += 1
                else:
                    orðabók[orð] = 1
    summaOrða = sum(orðabók.values())

    algengastaOrð = ""
    tiðni_algengasta = 0

    for orð, tíðni in orðabók.items():
        if tíðni > tiðni_algengasta:
            algengastaOrð = orð
            tiðni_algengasta = tíðni
    
    wordCount = 0
    for key in orðabók.values():
        if key > 1:
            wordCount +=1

    print("Fjöldi orðanna í skránni eru: ", summaOrða)
    print("Algengasta orðið er: ",algengastaOrð)
    print("Orð sem koma oftar fyrir en einu sinni eru: ", wordCount)
 

spurning7()
