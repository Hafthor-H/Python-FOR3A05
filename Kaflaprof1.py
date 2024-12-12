def rummalKulu():
    #Notandi setur inn radíus kúlunnar
    radius = float(input("Settu inn radíus kúlu til að sjá rúmmál hennar \nRadíus: "))
    #Rúmmal reiknast
    rummal = (4*3.14*radius**3)/3
    print("Þetta er rúmmálið á kúlunni þinni: ", round(rummal, 2))


def evenOrOdd():
    #Notandi slær inn tölu
    num = int(input("Settu inn tölu til að sjá hvort hún sé oddatala eða slétt tala \nTala: "))

    #If fallið gáir hvort þetta sé slétt tala eða ekki
    if num % 2 == 0:
        print("Þetta er slétt tala")
    else:
        print("Þetta er oddatala")

def sumOfNegativeAndPositive():
    #Skilgreina breytur
    num1Ja = 0
    num1Ne = 0
    num2Ja = 0
    num2Ne = 0
    num3Ja = 0
    num3Ne = 0
    num1= int(input("Settu inn þrjár heiltölur og sjáðu summu jákvæðu talnanna og summu neikvæðu talnanna. \nTala1: "))
    num2 = int(input("Tala2: "))
    num3 = int(input("Tala3: "))

    #Flokka tölurnar
    if num1 >= 0:
        num1Ja = num1
    if num1 < 0:
        num1Ne = num1

    if num2 >= 0:
        num2Ja = num2
    if num2 < 0:
        num2Ne = num2

    if num3 >= 0:
        num3Ja = num3
    if num3 < 0:
        num3Ne = num3

    #Finna summa jákvæðu og neikvæðu
    summaJa = num1Ja+num2Ja+num3Ja
    summaNe = num1Ne+num2Ne+num3Ne

    #Prenta útkomuna
    print("Summa jákvæðu: ",summaJa )
    print("Summa neikvæðu: ", summaNe)

def askDate():
    #Notandi slær inn upplýsingar
    dagur = int(input("Settu inn mánaðardag(tölur), mánuð(orð) og ár(tölur) \nDagur: "))
    manudur = str(input("Mánuður: "))
    ar = int(input("Ár: "))

    if dagur == 25 and manudur == "Október" and ar == 2024:
        print("Rétt")
    else:
        print("Rangt")



def sp3(): 
    summaJa = 0
    summaNe = 0
    num1= int(input("Settu inn þrjár heiltölur og sjáðu summu jákvæðu talnanna og summu neikvæðu talnanna. \nTala1: "))
    num2 = int(input("Tala2: "))
    num3 = int(input("Tala3: "))
    list = [num1,num2,num3]
    for i in list:
        if i >= 0:
            summaJa += i
        else:
            summaNe += i
    print("Summa jákvæða: ",summaJa)
    print("Summa neikvæða: ",summaNe)

sp3()