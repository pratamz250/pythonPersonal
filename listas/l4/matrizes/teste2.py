import random

m = [[0 for _ in range(2)] for _ in range(2)]

for i in range(2):
    for j in range(2):
        m[i][j] = random.randint(1, 100)

for i in range(2):
    print()
    for j in range(2):
        print(m[i][j], end=" ")

print()
