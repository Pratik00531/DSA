s = "abba"
def stringofpalindrome(s):
    if len(s) <= 1:
        return True
    else : 
        if s[::-1] == s:
            print("palindrome")
        else:
            print("Its not a palindrome")

stringofpalindrome(s)   