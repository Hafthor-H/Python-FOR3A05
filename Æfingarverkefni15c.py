import random


def hitastigManadar():
    listinn = []

    for i in range(12):
        addList = int(input("Hvert er meðalhitastigið: "))
        listinn.append(addList)

    print(max("\n Þetta er hæðsta hitastig mánaðar: ",listinn))
    print(min("Þetta er lægsta hitastig mánaðar:  ", listinn))



# Laga svo max sé tómur listi en ekki 0
def hitastigManadar2():
    max = 0
    listinn = []
    for i in range(12):
        addList = int(input("Hvert er meðalhitastigið: "))
        listinn.append(addList)

    for i in listinn:
        if i >= max:
            max = i
            continue

    min = max
    for i in listinn:
        if i <= min:
            min = i
            continue

    print("Þetta er hæðsta, ", max)
    print("Þetta er lægsta ", min)

def spilastokkur():
    sortir = ["Hjarta", "Spaði", "Tígull", "Lauf"]
    tölur = ["Ás","2","3","4","5","6","7","8","9","10","Gosi","Drottning","Kóngur"]
    veljaSort = random.choice(sortir)
    veljatölu = random.choice(tölur)
    print(veljaSort,veljatölu)

def ticTacToe():
    gameBoard = [[],[],[]]

    for i in range(3):
        for j in range(3):
            if (i +j) % 2 == 0:
                gameBoard[i].append("X")
            else:
                gameBoard[i].append("O")
    for i in gameBoard:
        for j in i:
            print(j, end = " ")
        print()


# def climbStairs( n):
#     step = 0
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     for i in range(n):
#         step +=i
#     return(step)

# print(climbStairs(5))

