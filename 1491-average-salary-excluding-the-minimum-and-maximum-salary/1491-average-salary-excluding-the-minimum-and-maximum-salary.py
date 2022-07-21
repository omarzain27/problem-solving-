class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        cnt = len(salary)
        avg = 0
        for i in range(1, cnt-1):
            avg +=salary[i]
        return (avg/(cnt-2))
