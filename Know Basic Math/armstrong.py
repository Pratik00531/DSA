print("Enter a number :")
sum = 0 
n = int(input())
arm = n 
for i in range(len(str(n))):
    digit = n % 10
    sum = sum + (digit * digit * digit )
    print(sum)
    n = n // 10

if sum == arm :
    print ("The number is an Armstrong number")
else:
    print ("The number is not an Armstrong number")