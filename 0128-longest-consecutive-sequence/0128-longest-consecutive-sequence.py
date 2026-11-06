class Solution(object):
    def longestConsecutive(self, nums):
        count = 0 
        max_count = 0
        s = set(nums)
        for num in s:
            if num-1 not in s:
                count = 1
                while num+count in s :
                    count +=1
                max_count = max(count ,max_count)
        return max_count
