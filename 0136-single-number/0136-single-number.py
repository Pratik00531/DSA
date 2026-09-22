class Solution(object):
    def singleNumber(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        for num,c in count.items():
            if c == 1:
                return num