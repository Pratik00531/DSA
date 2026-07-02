h = 6
for i in range(1,5):
    for j in range(i):
        print(str(j+1),end = " ")
    for k in range(i):
        print(" "*h + str(j+1), end = " ")
        h = h- 2
    print()