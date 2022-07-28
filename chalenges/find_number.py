"""def findNumber(arr, k):
    contem = False
    if k in arr:
        contem = True

    if contem:
        print('Yes')
    else:
        print('No')
"""


def findNumber(arr, k):
    if k in arr:
        return "YES"
    return "NO"


arr2 = [1, 2, 3, 4, 5]

print(findNumber(arr2, 0))
