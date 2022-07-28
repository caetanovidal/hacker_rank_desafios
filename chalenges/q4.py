products = ['a', 'a', 'a', 'b', 'c', 'c', 'c']

l = []
for i in products:
    if i not in l:
        l.append(i)
    l.sort()

maior = 0
indice = 0

for x in range(0, len(l)):
    qt = products.count(l[x])
    if qt >= maior:
        maior = qt
        indice = x

print(l[indice])
