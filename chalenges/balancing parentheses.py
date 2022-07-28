s = '()))'
p_esquerda = 0
p_direita = 0
for x in range(0, len(s)):
    if s[x] == '(':
        p_esquerda += 1
    else:
        p_direita += 1
if p_direita > p_esquerda:
    print(p_direita - p_esquerda)
if p_esquerda > p_direita:
    print(p_esquerda - p_direita)

