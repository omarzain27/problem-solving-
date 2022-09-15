class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        h = 0
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        for key in dic:
            for i in range(dic[key]):
                h += i
        return h