class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 1
        while i <=n:
            i *=3
            if i == n:
                return True
        return True if n == 1 else False
        