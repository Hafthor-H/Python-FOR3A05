#A hluti
def halda_afram_loop():
    haldaafram = "Y"
    while haldaafram != "N":
        tala = (input("Sláðu inn tölu"))
        print("þú hefur valið töluna: ", tala)
        haldaafram = input("Má bjóða þér að halda áfram Y/N? ")

#B hluti
def print_range_B():
    for Bi in range(5, 15, ):
        print(Bi)

#C hluti
def print_range_C():
    Ctala1 = int(input("Settu inn tvær tölur til að sjá allar tölurnar á því talnabili \nTala1: "))
    Ctala2 = int(input("Tala2: "))
    Cstokk = int(input("Stökk: "))
    for Ci in range(Ctala1, Ctala2, Cstokk):
        print(Ci)

#D hluti
def print_range_D():
    Dtala1 = int(input("Settu inn tvær tölur til að sjá allar tölurnar á því talnabili \nTala1: "))
    Dtala2 = int(input("Tala2: "))
    Dstokk = int(input("Stökk: "))

    if Dtala1 == Dtala2:
        print("Kjáni þetta er sama talan")
    elif Dtala1 == Dtala2-1 or Dtala2 == Dtala1-1:
        print("Bilið er bara 1 goofy ass")
    else:
        for Di in range(Dtala1, Dtala2, Dstokk):
            print(Di)

#E hluti
def print_range_E():
    Etala1 = int(input("Settu inn tvær tölur til að sjá allar tölurnar á því talnabili ásamt tölunum í ^2 \nTala1: "))
    Etala2 = int(input("Tala2: "))
    Estokk = int(input("Stökk: "))

    for Ei in range(Etala1, Etala2, Estokk):
        print(Ei)

    for Ei in range(Etala1**2, Etala2**2, Estokk):
        print("E tölur í ^2", Ei)

#F hluti
def sum_range_F():
    Ftala1 = int(input("Settu inn tvær tölur til að sjá summu talnabilsins \nTala1: "))
    Ftala2 = int(input("Tala2: "))
    Fstokk = int(input("Stökk: "))
    Fsum = sum(range(Ftala1, Ftala2, Fstokk))
    print(Fsum)


def sum_range_F_less_elegant():
    FEtala1 = int(input("Settu inn tvær tölur til að sjá summu talnabilsins \nTala1: "))
    FEtala2 = int(input("Tala2: "))
    FEstokk = int(input("Stökk: "))

    SummaFE = 0

    for Ei in range(FEtala1, FEtala2+1, FEstokk):
        SummaFE += Ei
    print("Þettta er summa talanbilsins:", SummaFE)


#G hluti



def factorial_range_G():
    Gtala1 = int(input("Settu inn tvær tölur til að sjá talnabilið ásamt tölunum hrópmerkt \nTala1: "))
    Gtala2 = int(input("Tala2: "))

    for factorOuter in range(Gtala1,Gtala2+1):
        hropmerkt = 1
        print("The number: ",factorOuter)
        for factorInner in range(1, factorOuter+1):
            hropmerkt *= factorInner
        print("Factorial of the number: ", hropmerkt)

#H hluti

def margföldunartafla():
    Htala = int(input("Settu inn tölu til að sjá margföldunartöfluna fyrir sá tölu: \nTala: "))
    
    for Hi in range(1,11):
        Hi *= Htala
        print(Hi)


#I hluti        

def margföldunartafla_2():

    for Ii in range(1,11):      
        for IiInner in range(1,11):
            print(IiInner*Ii, end=" ")
        print()
margföldunartafla()
