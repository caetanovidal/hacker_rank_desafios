def oddNumbers(l, r):
    # Write your code here
    arr = []
    for x in range(l, r+1):
        if x % 2 != 0:
            arr.append(x)
    return arr

l = 2
r = 5

oddNumbers(l, r)