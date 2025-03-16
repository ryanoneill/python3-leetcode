from typing import List
import math

class Solution:
    def canFinish(self, ranks: List[int], cars: int, time: int) -> bool:
        count = 0
        for rank in ranks:
            count += math.floor(math.sqrt(time // rank ))
        return count >= cars


    def repairCars(self, ranks: List[int], cars: int) -> int:
        lowest = min(ranks)
        left = 1
        right = lowest * cars * cars
        result = right

        while left <= right:
            mid = left + (right - left) // 2
            if self.canFinish(ranks, cars, mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
