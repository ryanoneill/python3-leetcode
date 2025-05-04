class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        result = 0

        m = len(s)
        n = len(t)

        cache = {}
        def worker(i: int, j: int) -> int:
            if j == n:
                return 1
            elif i == m:
                return 0
            else:
                result = 0

                key = (i, j)
                if key not in cache:
                    sletter = s[i]
                    tletter = t[j]
                    if sletter == tletter:
                        result += worker(i+1, j+1)
                    result += worker(i+1, j)
                    cache[key] = result
                return cache[key]

        result = worker(0, 0)
        return result
