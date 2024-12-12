#A hluti
haldaafram = "Y"
while haldaafram != "N":
    tala = (input("Sláðu inn tölu"))
    print("þú hefur valið töluna: ", tala)
    haldaafram = input("Má bjóða þér að halda áfram Y/N? ")

#B hluti
for Bi in range(5,15, ):
    print(Bi)

#C hluti
Ctala1 = int(input("Settu inn tvær tölur til að sjá allar tölurnar á því talnabili \nTala1: "))
Ctala2 = int(input("Tala2: "))
Cstokk = int(input("Stökk: "))

for Ci in range(Ctala1, Ctala2, Cstokk):
    print(Ci)

#D hluti 
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

Etala1= int(input("Settu inn tvær tölur til að sjá allar tölurnar á því talnabili \nTala1: "))
Etala2 = int(input("Tala2: "))
Estokk = int(input("Stökk: "))

for Ei in range(Etala1, Etala2, Estokk):
    print(Ei)


for Ei in range(Etala1**2, Etala2**2, Estokk):
    print("E tölur í ^2",Ei)
    
#F hluti
Ftala1 = int(input("Settu inn tvær tölur til að sjá summu talnabilsins \nTala1: "))
Ftala2 = int(input("Tala2: "))
Fstokk = int(input("Stökk: "))
for Fi in range(Ftala1, Ftala2, Fstokk):
    print(sum(Fi))