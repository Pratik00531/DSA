class Solution(object):
    def constructTransformedArray(self, nums):
        ans = []
        n = len(nums)
        for i in range(n):
            target = (i + nums[i]) % n
            ans.append(nums[target])
        return ans