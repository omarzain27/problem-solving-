class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        d = {i:chr(i+64)for i in range(1,27)}
        result = ""
        while columnNumber:
            temp = (columnNumber -1)%26
            result = result + d[temp+1]
            columnNumber = (columnNumber -1)// 26
        return result[ : :-1]
        
        