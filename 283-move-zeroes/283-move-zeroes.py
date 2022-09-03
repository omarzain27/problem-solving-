class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        if 0 in nums:
            x=nums.count(0)
        nums[:] = (i for i in nums if i !=0 )
        nums+=[0]*x
                