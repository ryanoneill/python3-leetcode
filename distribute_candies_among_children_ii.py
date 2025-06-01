import math

class Solution:
    def partition(self, n: int) -> int:
        result = 0
        if n > 0:
            result = math.comb(n, 2)
        return result

    def distributeCandies(self, n: int, limit: int) -> int:
        result = self.partition(n + 2)
        result -= 3 * self.partition(n - limit + 1)
        result += 3 * self.partition(n - 2 * (limit + 1) + 2)
        result -= self.partition(n - 3 * (limit + 1) + 2)

        return result
