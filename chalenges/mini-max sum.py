arr2 = [1, 3, 5, 7, 9]


def miniMaxSum(arr):
    maior = 0
    menor = 0
    for x in arr:
        if x == max(arr):
            maior = x
        if x == min(arr):
            menor = x
    print(f'{sum(arr) - maior} {sum(arr) - menor}')



miniMaxSum(arr2)
