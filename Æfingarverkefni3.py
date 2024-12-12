# 1 hluti
print("Choose a number")
number = int(input())

print("The answer to life, the universe, and everything is", number)
print(" \n \n")

# 2 hluti
print("Input two numbers to find there difference \nFirst number:")
tala_1 = input()
print("Now the second number:")
tala_2 = input()

divideOutput =  int(tala_1) - int(tala_2)
print(divideOutput)
print(" \n \n")

# 3 hluti
print("Input two numbers to add them together \nFirst number:")
tala_3 = input()
print("Now the second number:")
tala_4 = input()

addoutput = int(tala_3) + int(tala_4)
print(addoutput)
print(" \n \n")

# 4 hluti
print("Input two numbers to multiply them \nFirst number:")
tala_6 = input()
print("Now the second number:")
tala_7 = input()

multiplyOutput = int(tala_6) * int(tala_7)
print(multiplyOutput)
print(" \n \n")

# 5 hluti
print("Input your height and weight to find out how you do on the BMI scale ! \nInput your weight: ")
weight = input()
print("Now input your height")
height = input()

BMI = float(weight) / float(height)**2
print(BMI)
print(" \n \n")

# 6 hluti 
print("Input two integers to divide them and find the remainder \nFirst number:")
tala_8 = input()
print("Now the second number")
tala_9 = input()

divideOutput = float(tala_8) / float(tala_9)
divideRemainderOutput = float(tala_8) % float(tala_9)
print("Quotient:",round(divideOutput), "Remainder: ", divideRemainderOutput )
print(" \n \n")

# 7 hluti
print("Insert the price of an item to know the price after tax")
tala_10 = input()

afterTax = int(tala_10)*(1+0.255)
print("This is the price after tax:", afterTax)

