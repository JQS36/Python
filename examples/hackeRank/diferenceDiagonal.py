"""
1 2 3
4 5 6
9 8 9  

1 + 5 + 9 the left to right diagonal
3 + 5 + 9 the right to left diagonal

valor absoluto 15 - 17 = 2
"""

def absDiagonal(matrix):
    leftToRigth, rigthToLeft = 0, 0
    for i in range(len(matrix)):
        print(i , matrix[i], matrix[i][~i], ~i, sep=" <---> ")
        leftToRigth += matrix[i][i]
        rigthToLeft += matrix[i][~i]
    return abs(leftToRigth - rigthToLeft)

    """leftToRigth, rigthToLeft = 0, 0
    matrix_2 = []
    for i in range(len(matrix)):
        matrix_2.append(matrix[i][::-1])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                leftToRigth += matrix[i][j]
    for i in range(len(matrix_2)):
        for j in range(len(matrix_2)):
            if i == j:
                rigthToLeft += matrix_2[i][j]
    print(abs(leftToRigth-rigthToLeft))"""

matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(absDiagonal(matrix))