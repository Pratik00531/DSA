def ntoone(n):
    if n > 0:
        print(n,end = " ")
    else :
        return 1
    return ntoone(n-1)

if __name__ == "__main__":
    n = int(input("Enter a number:"))
    ntoone(n)
    