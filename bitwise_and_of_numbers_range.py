class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        m, n = left, right
        while m < n:
            n = n & (n - 1)

        return n
