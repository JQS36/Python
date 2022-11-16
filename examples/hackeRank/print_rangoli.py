"""
    Sample Input: 5
    Sample Output:
    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    --e-d-c-b-c-d-e--
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------
"""

import string 

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    letters = list(alphabet[:size][::-1])
    width = ((size * 2 - 1) * 2) - 1
    array = []
    for i in range(len(letters)):
        letter_modify = letters[:i+1]
        letter_modify += letter_modify[::-1][1:]
        array.append("-".join(letter_modify).center(width, "-"))
    print("\n".join(array), "\n".join(array[::-1][1:]), sep="\n")

print_rangoli(5)