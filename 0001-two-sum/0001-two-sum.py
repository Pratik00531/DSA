class Solution(object):
    def twoSum(self, nums, target):        
        results = []
        for i in range(len(nums)):
           a = target - nums[i]
           if a in nums and nums.index(a) != i:
            return [nums.index(a), i]
            