class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        result = True

        m = len(s1)
        n = len(s2)
        s = len(s3)

        result = (m + n) == s

        cache = {}
        def worker(i: int, j: int, k: int) -> bool:
            if k == s:
                return i == m and j == n
            else:
                key = (i, j, k)
                if key not in cache:
                    result = False
                    sletter = s3[k]
                    if i < m and s1[i] == sletter:
                        result = result or worker(i+1, j, k+1)
                    if j < n and s2[j] == sletter:
                        result = result or worker(i, j+1, k+1)
                    cache[key] = result
                return cache[key]

        result = result and worker(0, 0, 0)
        return result


