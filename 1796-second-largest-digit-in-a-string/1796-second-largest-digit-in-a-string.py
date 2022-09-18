class Solution:
    def secondHighest(self, s: str) -> int:
        count = 0
        s = sorted(s , reverse = True)
        for i in range(len(s)-1):
            if s[i] >='0' and s[i]<='9':
                if s[i] > s[i+1] :
                    return s[i+1]
        return -1
        