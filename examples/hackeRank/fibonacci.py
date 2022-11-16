def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    if n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

array = []
for i in range(1, 11):
    array.append(fibonacci(i))
print(",".join(map(str,array)))

# 1,1,2,3,5