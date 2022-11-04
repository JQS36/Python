#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    #[print("#"*(i+1), " "*(n-(i+1)), sep="") for i in range(n)]
    [print(str('#'*i).rjust(n)) for i in range(1,n+1)]
        
        

if __name__ == '__main__':
    n = int(input("Enter number: ").strip())
    staircase(n)