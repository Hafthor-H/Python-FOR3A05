def isInList():
    numList = [6, 5, 4, 3.]
    uInput = int(input("Sláðu inn tölu: "))
    if uInput in numList:
        print(uInput, "Er í listanum! ")
    else: 
        print(uInput, "Er ekki í listanum! ")

def elementInList():
    myList = []
    uInput1 = int(input("Sláðu inn tölu til að ákveða stærðina á listanum: "))

    for i in range(uInput1):
        uInput2 = int(input("Sláðu inn tölur fyrir listann: "))
        myList.append(uInput2)
    print(myList)


def sumOfElement():
    summa = 0
    listinn = []
    size = int(input("Hversu langur á listinn að vera: "))

    for i in range(size):
        addList = int(input("Tala: "))
        listinn.append(addList)
        summa += addList
    print(summa)

def averageOfList():
    summa = 0
    listinn = []
    size = int(input("Hversu langur á listinn að vera: "))
    
    for i in range(size):
        addList = int(input("Tala: "))
        listinn.append(addList)
        summa += addList
    newSum = summa / size
    print(newSum)

def highestValueOfList():
    max = 0
    listinn = []
    size = int(input("Hversu langur á listinn að vera: "))

    for i in range(size):
        addList = int(input("Tala: "))
        listinn.append(addList)

    for i in listinn:
        if i >= max:
            max = i
            continue   
    print(max)

