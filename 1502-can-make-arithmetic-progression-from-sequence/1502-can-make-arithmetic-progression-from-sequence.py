class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        flag = arr[1]-arr[0]
        for i in range(0 , len(arr)-1):
            if abs(arr[i]-arr[i+1]) == flag:
                print(i)
                continue
            else:
                return(0)
        return(1)
        