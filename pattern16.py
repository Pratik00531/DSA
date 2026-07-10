h = 0
n = 8
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print(" "*h,end="")
    h = h+2
    for k in range(i):
        print("*",end="")
    print()

for l in range(1,6):
    for m in range(l):
        print("*",end="")
    print(" "*n,end="")
    n = n-2
    for o in range(l):
        print("*",end="")
    print()    