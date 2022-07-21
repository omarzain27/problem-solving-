class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        arr=10000
        distance = 100000000
        flag = 0
        for i in range(0 , len(points)):
            if points[i][0] == x or points[i][1] == y:
                if abs(x-points[i][0])+abs(y-points[i][1]) < distance:
                    distance = abs(x-points[i][0])+abs(y-points[i][1])
                    arr=i
                    flag = 1
        if flag ==1: return(arr)
        else: return(-1)
        
        