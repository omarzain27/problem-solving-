class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Sum = 0
        product = 1
        while n >= 1:
            Sum += n % 10
            product *= n % 10
            n //= 10
        return (product - Sum)
        