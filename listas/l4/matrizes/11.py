import random

m = [[0 for _ in range(3)] for _ in range(3)]
ans = 0
count = 2

for i in range(3):
    for j in range(3):
        m[i][j] = random.randint(1, 100)

for i in range(3):
    if i > 0: 
        print()
    for j in range(3):
        print(m[i][j], end="  ")

print()

for i in range(3):
    ans += m[count][i]
    count -= 1

print(ans)
