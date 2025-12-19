maior = None
menor = None

for i in range(5):
    n = int(input())
    if i == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f"Maior: {maior}\nMenor: {menor}")
