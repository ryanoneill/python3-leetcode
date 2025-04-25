from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        above = 0
        counts = [0] * (101)
        for num in nums:
            if num <= 100:
                counts[num] += 1
            else:
                above += 1

        result = -1
        for i in range(100, 0, -1):
            above += counts[i]
            if i == above:
                result = i
                break
            elif i < above:
                break

        return result
