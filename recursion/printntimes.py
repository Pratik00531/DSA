def printnnumbers(n):
    if n>0:
        print(n)
    else:
        return 1
    
    return printnnumbers(n-1)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    printnnumbers(n)
