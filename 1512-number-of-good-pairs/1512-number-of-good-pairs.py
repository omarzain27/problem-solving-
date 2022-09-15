class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        res = 0
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        for key in dic:
            res += (dic[key]*(dic[key]-1))//2
        return res