class Solution(object):
    def sumCounts(self, nums):
        ans = []
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                subarray = []
                for  k in range(i , j+1):
                    subarray.append(nums[k])
                ans.append(subarray)
        distinct_counts = [len(set(sublist)) for sublist in ans]

        sum_of_squares = sum(x**2 for x in distinct_counts)
        return sum_of_squares        