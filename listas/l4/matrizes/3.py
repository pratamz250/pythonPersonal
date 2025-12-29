m = [[0 for _ in range(4)] for _ in range(4)]

for i in range(4):
    for j in range(4):
        m[i][j] = i*j

for i in range(4):
    print()
    for j in range(4):
        print(m[i][j], end=" ")

print()
