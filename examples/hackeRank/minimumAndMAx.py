


from array import array
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    hold = [None]*int(len(arr)-3)
    for i in range(0,len(arr)-3):
        temp = 0
        for j in range(i,i+4):
            print(i, arr[i], j, arr[j], sep=" <-> ")
            temp = temp + arr[j]
        hold[i] = temp
    
    print(hold[0],hold[-1], hold)
        


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    miniMaxSum(arr)