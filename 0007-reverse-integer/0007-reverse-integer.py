class Solution(object):
    def reverse(self, x):
        a = str(x)
        if a[0] == '-':
            result = int(a[0] + a[1:][::-1])
        else:
            result = int(a[::-1])

        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result   