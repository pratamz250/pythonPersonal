import random

def main():
    prints()
    fermiCount = 0
    picoCount = 0

    r = random.randint(100, 999)
    print(r)

    rArray = digits(r)
    """for i in range(3):
        print(rArray[i])"""

    print()
    for i in range(10):
        print(f"Guess #{i+1}: ")
        g = int(input())

        gArray = digits(g)

        for i in range(3):
            if rArray[i] == gArray[i]:
                fermiCount += 1

        if fermiCount == 0:
            rArray.sort()
            gArray.sort()

            for i in range(3):
                if rArray[i] == gArray[i]:
                    picoCount += 1

        if fermiCount == 0 and picoCount == 0:
            print("Bagels")
        if fermiCount > 0 and picoCount == 0:
            print("Pico")
        if fermiCount == 0 and picoCount > 0:
            print("Fermi")
        
        fermiCount = 0
        picoCount = 0

    print(f"Right number: {r}")

def prints():
    print("I'm thinking of a 3-digit number. Try to guess what it is.")
    print("Here are some clues:")
    print("When I say:     That means: ")
    print("Pico            One digit is corret but in the wrong position.")
    print("Fermi           One digit is correct but in the right position.")
    print("Bagels          No digit is correct.")
    print("I've thought up a number!")
    print("You have 10 guesses to get it.")

def digits(z):
    xs = [0] * 3

    #print(z)

    u = z%10
    xs[0] = u
    d = ((z - u)//10)%10
    xs[1] = d
    c = ((z - u) - (d*10))//100
    xs[2] = c

    return xs

if __name__ ==  "__main__":
    main()