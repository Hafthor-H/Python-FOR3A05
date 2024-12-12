def checkNum():
    while True:
        userInput = input("Sláðu inn heiltölu: ")
        try:
            num = int(userInput)
            print("Góður strákur:", num)
            break
        except ValueError:
            print("Ertu eitthvað heimskur \nÞetta var ekki flókið verkefni....")
            continue


def sumOfTwo(a,b):
    
    try:
        summa = a + b
        print(summa)
    except TypeError:
        print("\nÞetta er mismunandi breytur \n \n \nKJÁNI") 

        
sumOfTwo(4,5)

# def inputBoy():
#     print("Input two num for the sum:")
#     num1 = input("num1: ")
#     num2 = input("num2: ")
#     sumOfTwo(num1,num2)

# inputBoy()