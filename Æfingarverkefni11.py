#A hluti 

def halloHeimur():

    string = "Hallo Heimur!"

    for i in string:
        print(i)
    print(len(string))

#B hluti 

def santaAtNasa():
    
    string =  "A Santa at Nasa"

    for i in string[:: -1]:
        print (i)
    print("----------------------------------------------------------------------")
    for i in string[::1]:
        print(i)

#C hluti 

def userInput():
    texti = input("Settu inn texta og veldu svo hversu stór hluti af honum prentast. \nTexti: ")
    lengd = int(input("Lengd: "))

    for i in texti[:lengd]:
        print(i)

def bjagadurTexti():
    texti = input("Settu inn texta til að fá bjagaða útgáfu tilbaka \nTexti: ")
    step = int(input("Settu inn tölu: "))

    for i in texti[::step]:
        print(i)

#E hluti

def hastafirOgLagstafir():
    texti = input("Settu inn texta: ")
    val = input("Veldu Hástafi(H) eða lágstafi(L)")

    if val == "H":
        print(texti.upper)

    else:
        print(texti.lower)

#F hluti

def aldurOgStarf():
    nafn = str(input("Hvað heitir þú? "))
    aldur = str(input("Hvað ertu gamall? "))
    vinna = str(input("Hvað vinnur þú við? "))
    texti = "Þú heitir {0} ert {1} gamall og þú vinnur hjá {2}"

    print(texti.format(nafn, aldur, vinna))


#G hluti 

def checkForHello(texti):
    
    if "halló" in texti:
        return print("Það er halló í þessum texta")
    else:
        return print("það er ekki halló í þessum texta")

def checkDigitType(strengur):

    if strengur.isdigit():
        return print("Þetta er talnastrengur")
    elif strengur.isalpha():
        return print("Þetta er strengur")
    else:
        return print("What is this abomination")

checkDigitType("Hafþor")