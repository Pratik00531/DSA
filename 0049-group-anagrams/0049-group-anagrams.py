class Solution(object):
    def groupAnagrams(self, strs):
        s = []
        for i in range(len(strs)):
            s.append(sorted(strs[i]))
        
        result = []
        visited = [False] * len(s)
        
        for j in range(len(s)):
            if visited[j]:
                continue
            group = [strs[j]]
            visited[j] = True
            for k in range(j + 1, len(s)):
                if not visited[k] and s[j] == s[k]:
                    group.append(strs[k])
                    visited[k] = True
            result.append(group)
        
        return result   