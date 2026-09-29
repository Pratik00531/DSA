class Solution(object):
    def isAnagram(self, s, t):
        s1 = sorted(s)
        s2 = sorted(t)
        if (s1 == s2):
            return True
        else:
            return False