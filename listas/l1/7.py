n = 0
count = 0

for i in range(3):
    print("Digite: ", end=" ")
    aux = int(input())
    if aux > 0:
        n += aux
        count += 1

print(f"Media: {n/count:.2f}")
