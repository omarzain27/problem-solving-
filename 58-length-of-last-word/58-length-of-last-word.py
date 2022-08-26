class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)-1, -1 , -1):
            if s[i] >= 'a' and s[i] <= 'z' or s[i]>= 'A' and s[i]<= 'Z':
                cnt+=1
            if cnt > 0 and s[i] == ' ':
                return cnt
        return cnt