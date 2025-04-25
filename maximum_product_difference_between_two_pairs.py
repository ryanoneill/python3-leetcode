from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = -1
        max2 = -1

        min1 = 100000
        min2 = 100000

        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        result = (max1 * max2) - (min1 * min2)
        return result
