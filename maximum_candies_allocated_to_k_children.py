from typing import List

class Solution:
    def can_give(self, candies: List[int], k: int, amount: int) -> bool:
        if amount == 0:
            return True
        else:
            count = 0
            for candy in candies:
                count += candy // amount
                if count >= k:
                    break

            return count >= k

    def maximumCandies(self, candies: List[int], k: int) -> int:
        result = 0
        total = sum(candies)

        if total >= k:
            left = 0
            right = total // k

            while left <= right:
                mid = left + (right - left) // 2
                if self.can_give(candies, k, mid):
                    result = mid
                    left = mid + 1
                else:
                    right = mid - 1

        return result
