#convertir un numero dado en binario, y contar los numeros 1 consecutivos

from itertools import count
from unicodedata import name

if __name__ == "__main__":
    def getBaseTen(binaryVal):
        return int(binaryVal, 2)
        count = 0
        binaryVal = binaryVal[::-1]
        for i in range(0, len(binaryVal)):
            if(binaryVal[i] == "1"):
                count += 2**i
        return count
    try:
        number = int(input("Enter number: "))
        number_bin = bin(number)[2:]
        print("Number bin -> ", number_bin)
        print("Number return -> ",getBaseTen(number_bin))
        number_bin = max(number_bin.split("0"))
        print("Count 1 -> ",number_bin.count("1"))
    except:
        print("Is not int number")