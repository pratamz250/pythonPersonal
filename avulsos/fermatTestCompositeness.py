#Not naive at all (because we are in Python) programm to make the Fermat Test of Compositeness

import math

def main():
    n = int(input().strip())
    cong = set()
    count = 0

    for a in range(1, n):
        z = pow(a, n-1) % n
        #print(f"a:{a} congruence:{z}")
        cong.add(z)
        if z != 1:
            count += 1

    print(f"Set de numeros congruentes: {cong}")
    print(f"Congruencias: {len(cong)}")

if __name__ == "__main__":
    main()
