def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    print(character, string, sep="\n")
    string = string[:position] + character + string[position+1:]
    print(string[:position], string[position+1:])
    return string

string, position, character = "abracadabra", 2 ,"k"
print(mutate_string(string, position, character))