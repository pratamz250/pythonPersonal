def main():
    count = 0
    
    s1 = input()
    s2 = input()

    if len(s1) != len(s2):
        print("Diferent sizes")
        return 1
    else:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1

    if count > 1:
        print("1")
    else:
        print("0")

if __name__ == "__main__":
    main()

    print()
