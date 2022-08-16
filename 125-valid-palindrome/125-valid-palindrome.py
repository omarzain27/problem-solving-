class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(s)
        for i in range(0, len(s),):
            if (s[i] < 'a' or s[i] >'z') and (s[i]< '0' or s[i]>'9'):
                s[i] = ''
        s = [x for x in s if x != '']
        st = s[::-1]
        for i in range(len(s)):
            if st[i]!=s[i]:
                return False
        return True 