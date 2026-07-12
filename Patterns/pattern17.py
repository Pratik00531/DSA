n = 8
h = 2
for l in range(1,6):
    for m in range(l):
        print("*",end="")
    print(" "*n,end="")
    n = n-2
    for o in range(l):
        print("*",end="")
    print()    

for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    print(" "*h,end="")
    h = h+2
    for k in range(i):
        print("*",end="")
    print()