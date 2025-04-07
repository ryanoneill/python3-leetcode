from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        result = -1
        if n == 1:
            if nums == [1]:
                result = 0
        elif n == 2:
            if nums == [1, 1]:
                result = 0
        else:
            result = 0
            for i in range(n - 2):
                if nums[i] == 0:
                    result += 1
                    nums[i] = 1
                    nums[i + 1] ^= 1
                    nums[i + 2] ^= 1
            if nums[-2] != 1 or nums[-1] != 1:
                result = -1

        return result
