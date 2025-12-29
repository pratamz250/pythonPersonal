import random

m = [[0 for _ in range(4)] for _ in range(4)]
maior = 0
menor = 0

for i in range(4):
    for j in range(4):
        m[i][j] = random.randint(1, 500)
        
maior = m[0][0]
menor = m[0][0]

for i in range(4):
    for j in range(4):
        if m[i][j] > maior:
            maior = m[i][j]

        if m[i][j] < menor:
            menor = m[i][j]

print(f"Maior: {maior}\nMenor: {menor}\n")
