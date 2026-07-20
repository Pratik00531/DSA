def printnnames(n):
    if n > 0 :
        print("Pratik" , end = " ")
    else: 
        return 1
    return printnnames(n-1)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    printnnames(n)