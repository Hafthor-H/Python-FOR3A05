#B hluti
def brosandiApi():
    brosA = input("Er apinn þinn glaður J/N? ")
    brosB = input("Er apinn þinn glaður J/N? ")

    if brosA == "J" and brosB == "J":
        print("ALlir apar glaðir! Jibbí")
    if brosA == "N" or brosB == "N":
        print("Helmingurinn af öpnunum er glaðir")
    else:
        print("Bring out the bananas!")

def paloAlto():
    hitastig = int(input("Hversu heitt er úti? "))
    arstid = input("Er sumar J/N? ")

    if arstid == "J":
        if hitastig >= 60 and hitastig <= 100:
            print("Íkornarnir eru að leika sér ójáááá VECTOR!")
        else:
            print("Íkornarnir eru heima í tölvunni")
    else:
        if hitastig >= 60 and hitastig <= 90:
            print("Íkornarnir eru að leika sér ójáááá VECTOR!")
        else: 
            print("Íkornarnir eru heima í tölvunni")

def talnaBil():
    tala1 = int(input("Settu inn tölu litli strákur: "))
    tala2 = int(input("Duglegur, settu nú inn aðra tölu: "))

    for i in range(tala1,tala2+1):
        if i % 5 == 0:
            continue
        else:
            print(i)

def rannsakaTölur():
    tala1 = int(input("Settu inn tvær tölur til að rannsaka þær: "))
    tala2 = int(input("Seinni talan: "))
    
    if tala1 + tala2 ==666 or tala1-tala2 == 666 or tala2-tala1 == 666 or tala1 == 666 or tala2 == 666:
        print("Merki dýrsins!")
    else:
        print("Ekkert merkilegt því miður")

def skakbord():
    loop = 0
    while loop <= 3: 
        print("H S H S H S H S")
        print("S H S H S H S H")
        loop += 1

def skakbord2():
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                print("H", end=" ") 
            else:
                print("S", end=" ")
        print()



def longestSubstring():
    string = input("Input a string to find the length of the longest substring without repeating characters: ")
    for i in string:
        print(i)
