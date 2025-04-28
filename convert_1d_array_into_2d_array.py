from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        results = []
        if len(original) == m * n:
            i = 0
            for _ in range(0, m):
                results.append(original[i:i+n])
                i += n

        return results



