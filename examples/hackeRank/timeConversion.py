#!/bin/python3

import math
import os
import random
import re
import sys, datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

"""def timeConversion(s):
    t = datetime.datetime.strptime(s, "%I:%M:%S%p")
    return datetime.datetime.strftime(t, "%H:%M:%S")

print(timeConversion("07:05:45PM"))"""

"""if 0 == x:
if y == 10:
print("Yes")

if 0 == x:
    if y == 10:
        print("Yes")"""

try:
    temp = "5 degrees"
    cel = 0
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print("Perras")