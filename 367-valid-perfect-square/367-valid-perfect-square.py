class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(0 , pow(2 , 31)):
            if i*i == num:
                return True
            elif i*i > num:
                return False
        