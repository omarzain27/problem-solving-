class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        cnt =0 
        result = 0
        for i in range(0, len(accounts)):
            cnt = 0
            for j in range(0, len(accounts[i])):
                cnt += accounts[i][j]
            if cnt >= result:
                result = cnt
        return result 
                
        