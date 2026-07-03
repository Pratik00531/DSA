n = 6
for i in range (1,5):
    for j in range (i):
        print(j+1,end = "")
    print(" " * n , end = "")
    n = n - 2 
    for l in range(i,0,-1):
        print(l,end = "")
    print()