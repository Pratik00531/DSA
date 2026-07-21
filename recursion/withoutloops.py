def withoutloops(n):
    if n==0:
        return  
    withoutloops(n-1)
    print(n, end=" ")

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    withoutloops(n)


#  This code explains the recursive stack. As we get to know that how n = 5 ,4,3,2 ,1 and til 0 nothings gets printed.
# but as soon as the base case is reaached where return is called , the stack starts to prints itself . 
# 