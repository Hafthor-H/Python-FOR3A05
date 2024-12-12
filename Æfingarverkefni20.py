# A hluti
def Simabok():
    gameLoop = ""
    simaskra = {}
    while gameLoop != "Q":
        nameInput = input("Sláðu inn nafn og símanúmer \nSláðu inn Q til að hætta\nNafn: ")
        numberInput = input("Símanúmer: ")
        simaskra[nameInput] = numberInput
        gameLoop = input("Sláðu inn Q til að hætta: ")
    print(simaskra)


# B hluti 
def uppflettitafla():
    tafla = {"Hafþór": "843-8101", "Mamma": "899-5697", "Pabbi": "861-5698"}
    for i in tafla:
        print(i, tafla[i])

def uppflettitaflaMedItems():
    tafla = {"Hafþór": "843-8101", "Mamma": "899-5697", "Pabbi": "861-5698"}
    for key,value in tafla.items():
        print(f"{key.capitalize()}: {value}")

# C hluti

def uppflettitafla(key,dict):
    if key in dict:
        return True
    else:
        return False
    
def stjornaUpflettitöflu():
    tafla = {1: "1000", 2: "2000",3: "3000",4: "4000", 5: "5000"}
    numInput = int(input("Sláðu inn tölu til að gá hvort hún sé í töflunni. \nTala: "))
    
    if uppflettitafla(numInput,tafla):
        print("Þessi tala er í töflunni")
    else:
        print("Þessi tala er ekki í töflunni")

# D hluti

def summaValues():
    tafla = {1: 124, 2: 253, 3: 234, 4: 655}
    summa = 0
    for i in tafla:
        summa += tafla[i]
    print(summa)

def summaValuesMedValues():
    tafla = {1: 124, 2: 253, 3: 234, 4: 655}
    summa = sum(tafla.values())
    print(summa)

# E hluti

def summaKeys():
    tafla = {1: 124, 2: 253, 3: 234, 4: 655}
    summa = 0
    for i in tafla:
        summa += i
    print(summa)





def SvenniKodi():
    # gerum tóma orðabók
    orðabók = {}
    # hversu stór á orðabókin að vera ?
    fjöldi_para = int(input("Hversu mörg pör eru í orðabókinni ?"))
    # byggjum upp orðabók (svipað og þegar um lista er að ræða)
    for i in range(fjöldi_para):
        # fáum að vita næsta lykil
        næsti_lykill = int(input("Sláðu inn næsta lykil, verður að vera heiltala takk fyrir. "))
        # ... og næsta gildi
        næsta_gildi = float(input("Sláðu inn næsta gildi, má vera hvaða tala sem er."))
        # stofnum nýjan lykil
        orðabók[næsti_lykill] = næsta_gildi
        # gerum breytu til að geyma summuna
        summa_gilda = 0
        # göngum yfir orðabókina okkar
    for lykill in orðabók:
        # bætum hverju gildi við summuna
        summa_gilda += orðabók[lykill]
        # tilkynnum notanda í lokin niðurstöðuna
    print("Summa gildanna í orðabókinni er: ", summa_gilda)

