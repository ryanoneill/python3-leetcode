from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        result = [0] * n

        for num in nums:
            if num % 2 == 0:
                result[left] = num
                left += 1
            else:
                result[right] = num
                right -= 1

        return result
