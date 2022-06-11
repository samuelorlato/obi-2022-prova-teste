n, m = [int(i) for i in input().split()]

ruas = []
for _ in range(n):
    ruas.append(input().split())

precos = []
preco = 0
for j in range(len(ruas[0])):
    for i in range(len(ruas)):
        preco += int(ruas[i][j])

    precos.append(preco)
    preco = 0

precos.sort()
print(precos[0])
