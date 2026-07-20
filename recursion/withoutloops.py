def withoutloops(n):
    if n==0:
        return  
    withoutloops(n-1)
    print(n, end=" ")
    
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    withoutloops(n)
