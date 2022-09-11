class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        dic = {}
        for i in range(len(boxes)):
            if boxes[i] > '0':
                dic[i] = 1
        for i in range(len(boxes)):
            val = 0
            for j in dic:
                val += abs(j-i)
            res.append(val)
        return res
        