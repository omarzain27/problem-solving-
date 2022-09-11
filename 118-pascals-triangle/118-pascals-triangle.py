class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return[[1],[1 , 1]]
        res = [[1] , [1 ,1]]
        for i in range(1,numRows-1):
            curr = [1]
            for j in range(0,len(res[i])-1):
                curr.append(res[i][j]+res[i][j+1])                
            curr.append(1)
            res.append(curr)
        return res
        