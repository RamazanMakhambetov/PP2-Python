class Solution(object):
    def subtractProductAndSum(self, n):
        n = [int(digit) for digit in str(n)]
        return functools.reduce(lambda x, y: x * y, n) - sum(n)