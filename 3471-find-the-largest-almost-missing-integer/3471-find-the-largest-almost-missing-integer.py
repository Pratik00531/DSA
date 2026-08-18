class Solution(object):
    def largestInteger(self, nums, k):
        # Case 1: The entire array is the only subarray
        if len(nums) == k:
            return max(nums)
        
        # Case 2: Subarrays of size 1 
        # We must find the largest number that has a global count of exactly 1
        if k == 1:
            ans = -1
            for x in nums:
                if nums.count(x) == 1:
                    ans = max(ans, x)
            return ans
        
        # Case 3: 1 < k < len(nums)
        # Only the absolute first or absolute last elements can belong to exactly one subarray
        first = nums[0]
        last = nums[-1]
        a = -1
        b = -1
        
        if nums.count(first) == 1:
            a = first
        if nums.count(last) == 1:
            b = last
            
        return max(a, b)
