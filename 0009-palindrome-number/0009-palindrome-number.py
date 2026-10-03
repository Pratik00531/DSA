class Solution(object):
    def isPalindrome(self, x):
        s=str(x)
        return x>=0 and s==s[::-1]