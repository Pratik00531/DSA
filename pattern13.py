h = 3
for i in range(1,5):
    for j in range(i):
        print(" "*h + chr(64+i),end ="")
        h = h - 1
    print()
