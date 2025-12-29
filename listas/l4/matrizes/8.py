import random

m = [[0 for _ in range(3)] for _ in range(3)]
count = 0

for i in range(3):
    for j in range(3):
        m[i][j] = random.randint(1, 400)
        if i > j:
            count += m[i][j]

print(f"Soma: {count}")
