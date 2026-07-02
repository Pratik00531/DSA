start = 1
for i in range(1,6):
    if i % 2 == 0 :
        start = 1
    else:
        start = 0
    for j in range(i):    
        start = 1 - start
        print(start, end = " ")
    print()