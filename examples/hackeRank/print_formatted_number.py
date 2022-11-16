def print_formatted(number):
    max_len = len(bin(number)[2:])
    for i in range(1, number+1):
        print(str(i).rjust(max_len), oct(i)[2:].rjust(max_len), hex(i)[2:].upper().rjust(max_len), bin(i)[2:].rjust(max_len))
       
print_formatted(12)