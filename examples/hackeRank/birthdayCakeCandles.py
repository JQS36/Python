#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

#return max count, all integers
def birthdayCakeCandles(candles):
    max_candles = str(max(candles))
    candles = "-".join(map(str, candles))
    result = re.findall(max_candles, candles)

    
    print(len(result))
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #candles_count = int(input().strip())

    #candles = list(map(int, input().rstrip().split()))
    candles = [82, 49, 82, 82, 41, 82, 15, 63, 38, 25]

    birthdayCakeCandles(candles)

    #fptr.write(str(result) + '\n')

    #fptr.close()
