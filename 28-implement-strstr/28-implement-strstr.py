class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        for i in range(0, len(haystack)):
            if haystack[i:length+i] == needle:
                return i
        return -1 if length > 0 else 0
        