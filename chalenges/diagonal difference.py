from random import randint
"""
Calcula a diagonal principal da matriz
e a digonal secundaria, depois faz a diferença em modulo das duas
"""
arr = [[-1, 1, -7],
       [-10, -8, -5],
       [0, 9, 7]]


def dif_diagonal(arr):

    dig_pri = []
    dig_sec = []

    for l in range(len(arr)):
        for c in range(len(arr)):
            if l == c:
                dig_pri.append(arr[l][c])
            if l + c == len(arr) - 1:
                dig_sec.append(arr[l][c])

    return abs(sum(dig_pri) - sum(dig_sec))


print(dif_diagonal(arr))
