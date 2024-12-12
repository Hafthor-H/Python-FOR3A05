#A hluti
print("Settu inn gallon til að komast að hvað það er í lítrum \nGallon:")
gallon = float(input())

litrar = gallon*3.6
print(round(litrar, 2))


#ARétt
print("Settu inn litra til að komast að hvað það er í gallon \nLitrar: ")
litrarA2 = float(input())

gallonA2 = litrarA2 / 3.6
print(round(gallonA2,2 ))


#B hluti
print("Settu inn radius hrings til að finnna flatarmáls hans:")
radius = int(input())

flatarmalHrings = radius*radius*3.14
print(flatarmalHrings)

#C hluti
print("Finndu flatarmál trapísu með því að gefa upp skammhlið, langhlið og hæð")
skammhlið = float(input("Skammhlið:"))
langhlið = float(input("Langhlið:"))
haed = float(input("Hæð:"))

flatarmaltrapisu = (skammhlið + langhlið) * haed / 2
print(flatarmaltrapisu)

#D hluti
print("Settu inn hitastig í farenheit til að vita það í celcius")
Tf = float(input("Farenheit:"))

Tc = (5/9)*(Tf-32)
print(round(Tc, 2))

#E hluti
print("Skrifaðu inn veldi og veldistofn og fáðu svar!")
veldisstofn = float(input("Veldisstofn:"))
veldi = float(input("Veldi: "))

veldisSvar = veldisstofn**veldi
print(veldisSvar)

#F hluti
print("Þetta er reiknivél skattsins. Settu inn álagningarprósentu, persónuafslátt og laun til að finna staðgreiðsluna þína")
alaging = float(input("Alagning (%): ")) / 100
aflslattur = int(input("Persónuafsláttur: "))
laun = int(input("Launaupphæð: "))
greidlsa = (laun * alaging)-aflslattur

if greidlsa > 0:
    print("Þú átt að borga:",greidlsa, "kr Til skattman")
elif greidlsa < 0:
    print("Þú átt", abs(greidlsa)," eftir af persónuafslætti")
else: 
    print("How did we get here?")

#G hluti
print("Hvaða tvö orð langar þig að birta í terminalið?")
word1 = input("Fyrsta orðið: ")
word2 = input("Seinna orðið: ")

print(word1)
print(word2)