import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def plusMinus(arr):
    count_min, count_max, count_zero = 0, 0, 0
    for i in range(len(arr)):
        if arr[i] < 0:
            count_min +=1
        elif arr[i] > 0:
            count_max +=1
        else:
            count_zero +=1  
    
    count_min = '{0:.6f}'.format(count_min / len(arr))
    count_max = '{0:.6f}'.format(count_max / len(arr))
    count_zero = '{0:.6f}'.format(count_zero / len(arr))
    array = "\n".join([count_max, count_min, count_zero])
    print(array) 

plusMinus([0, 0, -1, 1, 1])