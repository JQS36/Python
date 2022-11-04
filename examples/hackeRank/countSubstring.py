def count_substring(string, sub_string): 
    counter = 0
    print(dir(string))
    for i in range(len(string)):
        if i == string.find(sub_string,i,len(string)):
            counter += 1
    return counter

print(count_substring("jorgejorgejusn", "j"))