arr = [4, 1, 3, 2, 2]

arrcc = sorted(arr)
arrcc[0] = 1

for x in range(1, len(arrcc)-1):
    if arrcc[x+1] - arrcc[x] > 1:
        arrcc[x+1] = arrcc[x] + 1
print(max(arrcc))