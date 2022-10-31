import re

def validateEmail(s):
    return True if re.search("^[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$", s) else False

print(validateEmail("jorge@hotmail.com"))