

print("Þetta er reiknivél.\n Veldu hvað þú vilt reikna\n + \n - \n / \n *\n or Q to quit" )
sign = input()

while sign != "Q":

    if sign == "+": 
        print("Choose two numbers to add together \n")
        print("Choose the first number")
        num1 = input()
        print("Choose the second number")
        num2 = input()
        sum = int(num1)+int(num2)
        print(sum)
    
    if sign == "-":
        print("Choose two numbers to subtract")
        print("Choose the first number")
        num1 = input()
        print("Choose the second number")
        num2 = input()
        sum = int(num1)-int(num2)
        print(sum)

    if sign == "*":
        print("Choose two numbers to multiply")
        print("Choose the first number")
        num1 = input()
        print("Choose the second number")
        num2 = input()
        sum = int(num1)*int(num2)
        print(sum)

    if sign == "/":
        print("Choose two numbers to divide")
        print("Choose the first number")
        num1 = input()
        print("Choose the second number")
        num2 = input()
        sum = int(num1)/int(num2)
        print(sum)

    else: print("Goodbye!")
    break
