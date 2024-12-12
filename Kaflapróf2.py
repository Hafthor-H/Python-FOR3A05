

def spurning1():
    strengur = str(input("Sláðu inn streng: "))
    heiltala = int(input("Sláðu inn heiltölu: "))
    print(strengur[:2]*heiltala)

def spurning2():
    upphaf = int(input("Sláðu inn upphaf talnabils: "))
    endir = int(input("Sláðu inn enda talnabils: "))

    for i in range(upphaf,endir+1):
        if i % 4 == 0 or i % 7 == 0:
            continue
        else:
            print(i)

def spurning3():
    upphaf = int(input("Sláðu inn upphaf talnabils: "))
    endir = int(input("Sláðu inn enda talnabils: "))
    margfeldi = 1
    for i in range(endir, upphaf-1, -1):
        margfeldi *= i
        print(i)
    print(margfeldi)


def lengdStrengs(strengur):
    count = 0
    for i in strengur:
        count += 1
    return count

def callingString():
    userInput = input("Sláðu inn streng: ")
    length = lengdStrengs(userInput)
    print(f"Strengurinn er: {length}" )

# Það er mjög gagnlegt að nota föll í forritun þar sem þú getur endurnotað þau eins og oft hentar.
# Í staðinn fyrir að vera skrifa sama kóðan aftur og aftur þá frekar skrifa hann einu sinni sem fall og kalla á fallið.