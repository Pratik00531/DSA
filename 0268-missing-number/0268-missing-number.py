class Solution(object):
    def missingNumber(self, nums):
        ans = list(range(len(nums) + 1))
        return list(set(ans) - set(nums))[0]   