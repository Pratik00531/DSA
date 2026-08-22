class Solution(object):

    def validMountainArray(self, arr):

        if len(arr) < 3:
            return False

        largest = max(arr)
        peak = arr.index(largest)

        if peak == 0 or peak == len(arr) - 1:
            return False

        # Left side: increasing
        for i in range(peak):
            if arr[i] >= arr[i + 1]:
                return False

        # Right side: decreasing
        for i in range(peak, len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                return False

        return True