class Solution(object):
    def isPossibleToSplit(self, nums):
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1

            if count[x] > 2:
                return False

        return True