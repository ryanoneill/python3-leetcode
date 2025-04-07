from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def worker(index: int, current: int, n: int) -> int:
            result = 0
            if index == n:
                result = current
            else:
                value = nums[index]
                result += worker(index + 1, current ^ value, n)
                result += worker(index + 1, current, n)
            return result

        n = len(nums)
        result = worker(0, 0, n)

        return result
