def sumOfThree(num1, num2, num3):
        calc = num1 + num2 + num3
        return calc

# tala1 = int(input("Sláðu inn tölu: "))
# tala2 = int(input("Sláðu inn tölu: "))
# tala3 = int(input("Sláðu inn tölu: "))
# print("Þetta er summa talnanna ", end="")
# print(sumOfThree(tala1, tala2, tala3))

def profaBil(t, b, e):
        if t >= b and t <= e:
            return True
        else:
            return False
        
byrjun = int(input("Settu inn byrjun á bilinu "))
endir = int(input("Settu inn endan á bilinu "))
tala = int(input("Settu inn tölu til að sjá hvort hún sé á bilinu "))
if profaBil(tala, byrjun, endir):
      print("Talan er á bilinu! ")
else:
    print("Talan er ekki á bilinu :(")