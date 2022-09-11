class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        res = []
        for i in digits:
            s = s + str(i)
        s = int(s)+1
        for i in str(s):
            res.append(i)
        return res