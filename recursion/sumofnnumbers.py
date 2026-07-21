def sumofnnumbers(n):
    if n == 0:
        return 0
    else:
        return (n*n*n) + sumofnnumbers(n-1)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(sumofnnumbers(n))