

def margfoldun(num):
    for i in range(1, 11):
        print(num*i, end=" ")
    print()
# num = input("Settu inn tölu og sjáðu þá línu úr margföldunartöflunni ")
# margfoldun(3)

def margfoldun2():
    for i in range(1, 11):
        margfoldun(i)

def talnabil(b, e):
    for i in range(b,e+1,1):
        print(i, end=" ")

# talnabil(1,10)

def talnabil2(b2, e2):
    if b2 == e2:
        print("Ertu eitthvað heimskur")
    elif b2 == e2-1 or e2 == b2-1:
        print("gOoFy aSs")
    elif b2 > e2:
        print("Hvernig gerist þetta bara, Hugsa smá!")
    elif b2 < e2:
        print("Góður strákur hér eru tölurnar: ")
        for i in range(b2+1, e2):
            print(i, end=" ")

# tala1 = int(input("Settu inn byrjun á bilinu: "))
# tala2 = int(input("Settu inn endan á bilinu: "))

# talnabil2(tala1, tala2)

def veldi(tala, veldi):
    constTala = 1
    for i in range(veldi):
        constTala *= tala
    print(constTala)    

        

veldi(2,3)
