def plusMinus(arr):
    positivo = 0
    negativo = 0
    neutro = 0
    for x in arr:
        if x > 0:
            positivo += 1
        if x < 0:
            negativo += 1
        if x == 0:
            neutro += 1

    print(f'{positivo/len(arr):.6f}'
          f'\n{negativo/len(arr):.6f}'
          f'\n{neutro/len(arr):.6f}')


arr2 = [1, 1, 0, -1, -1]

plusMinus(arr2)
