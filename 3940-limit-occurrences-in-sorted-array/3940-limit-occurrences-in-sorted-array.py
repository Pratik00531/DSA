class Solution(object):
    def limitOccurrences(self, nums, k):
        result = []
        count = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                count = 1
                result.append(nums[i])
            elif count < k:
                count += 1
                result.append(nums[i])
        return result