count = 0

s = input()

for c in s:
    if (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
        #print(f"{c} -> {ord(c)}")
        count += 1

print(f"Letras: {count}")
