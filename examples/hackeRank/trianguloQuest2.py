"""
You are given a positive integer N.
Your task is to print a palindromic triangle of size .

For example, a palindromic triangle of size N is:

1
121
12321
1234321
123454321
"""

N = 5
for x in range(1,int(N)+1):
    var1 = 10 ** x
    var2 = (( var1 - 1) // 9)
    var3 = var2 ** 2
    print(var3)