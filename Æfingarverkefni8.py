
def nidurtalning():
    num1 = int(input("Settu inn tölu og ég skal telja frá henni niður að núll \nTala: "))

    while num1 != 0:
        print(num1)
        num1 -= 1
        

def oddatölur():
    low = int(input("Hvar byrjar bilið: "))
    high = int(input("Hvar endar bilið: "))
    #Gerum teljarabreytu
    teljari = low
    #Göngum yfir bilið
    while teljari <= high:
        #Prentum hverja tölu ef hún er oddatala
        if teljari % 2 == 1:
            print(teljari)
        #Hækkum teljara um 1
        teljari += 1

def forOddatölur():
    low = int(input("Hvar byrjar bilið: "))
    high = int(input("Hvar endar bilið: "))
    #Gerum teljarabreytu
    teljari = low
    #Göngum yfir bilið
    for teljari in range(low, high+1):
        #Prentum hverja tölu ef hún er oddatala
        if teljari % 2 == 1:
            print(teljari)
        #Hækkum teljara um 1
        teljari += 1

def sumOfRange():
    low = int(input("Settu inn tvær tölur til að sjá summu bilsins \nTala1: "))
    high = int(input("Tala2: "))
    summa = 0
    while low != high+1:
        summa += low
        low += 1
    print(summa)

def sumOfEven():
    low = int(input("Settu inn tvær tölur til að sjá summu allra sléttu talnana á bilinu \nTala1: "))
    high = int(input("Tala2: "))
    summaEven = 0
    teljari = low

    while teljari <= high:
        if teljari % 2 == 0:
            summaEven += teljari
        
        teljari +=1
    print(summaEven)

def theBomb():
    timer = int(input("Stilltu sprengjunna: "))
    while timer != 0:
        print(timer)
        timer -= 1
    print("Bombaclat!")

def findAnswer():
    num1 = 0
    while num1 != 42:
        num1 = int(input("Settu inn tölu: "))
        print("Þetta er talan þín", num1)
    print(num1, "Er svar lífsins og tilverunnar")

findAnswer()