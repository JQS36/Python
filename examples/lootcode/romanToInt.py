"""


Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


class Solution:

    def __init__(self, s):
        print(self.romanToInt(s))

    def romanToInt(self, s: str) -> int:
        rt = 0
        rd = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        for i in range(n):
            if  i == n-1 or rd[s[i]] >= rd[s[i+1]] :
                rt += rd[s[i]]
            else :
                rt -= rd[s[i]]
        return rt
 
Solution("IIIXIV")