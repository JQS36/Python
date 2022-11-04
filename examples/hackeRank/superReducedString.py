
#aaabccddd → abccddd → abddd → abd

def superReducedString(s):
    print(s)
    if len(s) < 1:
        return "Empty String"
    else:
        for i in range(0, len(s)-1):
            print(i)
            if s[i] == s[i+1]:
                print(i, s[i], s[i+1], s[:i], s[i+2:], s[:i]+s[i+2:],sep=" <-> ")
                return superReducedString(s[:i]+s[i+2:])
        return s

string = "aaabccddd"
print(superReducedString(string))