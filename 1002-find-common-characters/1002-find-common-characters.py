class Solution(object):
    def commonChars(self, words):
        common = []
        for ch in words[0]:
            if common.count(ch) < min(word.count(ch) for word in words):
                common.append(ch)
        return common   