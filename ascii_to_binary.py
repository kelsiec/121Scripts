name = None
while name != 'n':
    name = input("Enter a name (or 'n' to exit): ")

    print("Decimal Representation: ", end="")
    for char in name:
        print(str(ord(char)) + " ", end="")

    print("\nBinary Representation: ", end="")
    for char in name:
        print(bin(ord(char)) + " ", end="")
    print()
