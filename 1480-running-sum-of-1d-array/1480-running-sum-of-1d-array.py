class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sol = []
        SUM = 0
        for i in range (0 , len(nums)):
            for j in range (0, i+1):
                SUM += nums[j]
            sol.append(SUM)
            SUM =0
        return sol