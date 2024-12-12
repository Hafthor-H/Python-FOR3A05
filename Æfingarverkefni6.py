#A Hluti
print("Hvað er klukkan?")
klukka = int(input())

if klukka <= 18:
    print("Góðann daginn")

else:
    print("Gott kvöld")

#B hluti
print("Hvað er klukkan?")
klukka = int(input())

if klukka < 0 or klukka > 24:
    print("Invalid input")

elif klukka < 18:
    print("Góðann daginn")

elif klukka >= 18:
    print("Gott kvöld")

#C hluti
print("Settu inn tvær heiltölur til að sjá hvor er minni")
Ctala1 = int(input("Tala1: "))
Ctala2 = int(input("Tala2: "))

if Ctala1 == Ctala2:
    print("Þetta er sama talan kjáni")
elif Ctala1 < Ctala2:
    print("Tala1 er minni")
elif Ctala1 > Ctala2:
    print("Tala 2 er minni")

#D hluti 
print("Settu inn þrjár heiltölur til að sjá hver er minnst")
Dtala1 = int(input("Tala1:"))
Dtala2 = int(input("Tala2:"))
Dtala3 = int(input("Tala3:"))

print("Þetta er minnsta talan:",min(Dtala1,Dtala2,Dtala3))

print("Settu inn þrjár heiltölur til að sjá hver er minnst")
D2tala1 = int(input("Tala1: "))
D2tala2 = int(input("Tala2: "))
D2tala3 = int(input("Tala3: "))

# Manually compare the three numbers to find the smallest
if D2tala1 <= D2tala2 and D2tala1 <= D2tala3:
    D2smallest = D2tala1
elif D2tala2 <= D2tala1 and D2tala2 <= D2tala3:
    D2smallest = D2tala2
else:
    D2smallest = D2tala3

print("Þetta er minnsta talan:", D2smallest)


#E hluti
print("Hvað ert þú gamall?")
Ealdur = int(input("Aldur: "))

if Ealdur >= 0 and Ealdur <= 19:
    print("vonandi ætlar þú í Háskólann í Reykjavík")
else:
    print("Þetta var fróðlegt!")

#F hluti
print("Hvað ert þú gamall?")
Faldur = int(input("Aldur: "))

if Faldur >= 0 and Faldur <= 6:
    print("Nú, svo þú ferð að byrja í skóla")
elif Faldur >= 7 and Faldur <= 15:
    print("Ætlar þú í menntaskóla?")
    Spurning = input("Y/N?")
    if Spurning != "Y" and Spurning != "N":
        print("Invalid input")
    elif Spurning == "Y":
        print("Smartypants")
    else:
        print("Welcome to the 9-5")
elif Faldur >= 16 and Faldur <= 105:
    print("Goooodbye!")
else:
    print("Ertu að bulla í mér?")

#G hluti
print("Settu inn ár og sjáum hvort það sé hlaupaár eða ekki")
Gyear = int(input("Ár: "))

if Gyear % 4 == 0:
    print("Þetta er hlaupaár")
else:
    print("Þetta er ekki hlaupaár")

#H hluti
print("Settu inn ár og sjáum hvort það sé hlaupaár eða ekki")
Hyear = int(input("Ár: "))

if Hyear % 4 != 0:
    print("Árið er ekki hlaupaár")
elif Hyear % 100 == 0 and Hyear % 400 != 0:
    print("Árið er ekki hlaupaár")
else:
    print("Þetta er hlaupaár")