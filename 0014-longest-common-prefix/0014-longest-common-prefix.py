import os
class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = os.path.commonprefix(strs)
        return prefix
        