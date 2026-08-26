class Solution(object):
    def divideArray(self, nums):
        nums.sort()
        for i in range(0, len(nums), 2):   # ← 2 ke 2 aage
            if nums[i] != nums[i+1]:       # ← elements compare karo
                return False
        return True   