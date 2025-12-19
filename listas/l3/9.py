i = 1
count = 0
n = int(input())

while True:
    if i % 2 != 0:
        print(i)
        count += 1

    i += 1

    if count >= n:
        break
