class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return[1 , 1]
        res = [[1] , [1 ,1]]
        for i in range(1,rowIndex):
            curr = [1]
            for j in range(0,len(res[-1])-1):
                curr.append(res[i][j]+res[i][j+1])                
            curr.append(1)
            res.append(curr)
        return res[rowIndex]