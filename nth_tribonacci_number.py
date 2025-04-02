class Solution:
    def tribonacci(self, n: int) -> int:
        result = 0
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        elif n == 2:
            result = 1
        else:
            minus_one = 1
            minus_two = 1
            minus_three = 0
            for _ in range(3, n+1):
                result = minus_three + minus_two + minus_one
                minus_three = minus_two
                minus_two = minus_one
                minus_one = result

        return result

