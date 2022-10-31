def isNumberOdd(number):#impar
    return True if number%2==1 else False

def isNumberEven(number):
    return True if number%2==0 else False

n = int(input("Enter number: "))
print("Es numero impar: ", isNumberOdd(n))
print("Es numero par: ", isNumberEven(n))