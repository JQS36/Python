"""Sample Input

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Sample Output

AB
CA
AD"""

import textwrap

def merge_the_tools(string, k):
    """wrapper = textwrap.TextWrapper(width=k)
    word_list = wrapper.wrap(text=string)
    at = list( set(i) for i in word_list )
    [print("".join(a)) for a in at]"""

    for i in range(0,len(string),k):
        t = string[i: i+k]
        u = list(dict.fromkeys(t))
        print(t, u , sep=" -> ")
        print("".join(u))

merge_the_tools("AABCAAADA", 3)