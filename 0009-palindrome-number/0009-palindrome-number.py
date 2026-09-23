class Solution(object):
    def isPalindrome(self, x):
        y = str(x)
        if(x>=0):
            if(y[::-1] == y):
                return True
            else:
                return False
        else:
            return False
        