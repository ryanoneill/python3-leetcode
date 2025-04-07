from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            middle = left + ((right - left) // 2)

            spent = 0
            for pile in piles:
                spent += math.ceil(pile / middle)

            possible = spent <= h
            if possible:
                right = middle
            else:
                left = middle + 1

        return left
