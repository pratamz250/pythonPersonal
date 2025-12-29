m = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        if i == j: 
            m[i][j] = 1
        else:
            m[i][j] = 0

for i in range(5):
    print()
    for j in range(5):
        print(m[i][j], end=" ")


print()
