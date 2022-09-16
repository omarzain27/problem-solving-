class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        res = []
        ans = 0
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] +=1
        plus = 0
        for i in d:
            if d[i] ==1:
                plus = 1
            elif d[i]%2==0:
                ans+=d[i]
            else:
                ans+=d[i]-1
                plus =1
        return ans+plus