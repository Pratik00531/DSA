h = 3

for i in range(1, 5):

    print(" " * h, end="")
    h -= 1

    for j in range(i):
        print(chr(65 + j), end="")

    for k in range(i - 2, -1, -1):
        print(chr(65 + k), end="")

    print()