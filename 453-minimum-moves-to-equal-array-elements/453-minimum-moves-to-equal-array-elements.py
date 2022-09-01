class Solution:
    def minMoves(self, nums: List[int]) -> int:
        Min = min(nums)
        cnt = 0
        for i in range( 0 ,len(nums)):
            cnt+= nums[i] - Min
        return cnt