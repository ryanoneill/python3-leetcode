from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) // 2
        m = len(set(candyType))

        result = min(m, n)
        return result


