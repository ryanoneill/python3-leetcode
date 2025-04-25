import math


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7

        cache = {}

        def worker(current: int, possibilities: int) -> int:
            key = (current, possibilities)
            if key in cache:
                return cache[key]
            else:
                result = math.comb(n - 1, possibilities - 1)
                if possibilities < n:
                    next = current + current
                    while next <= maxValue:
                        result += worker(next, possibilities + 1)
                        next += current

                cache[key] = result
                return result

        result = 0
        for i in range(1, maxValue + 1):
            result += worker(i, 1)
        result = result % MOD

        return result
