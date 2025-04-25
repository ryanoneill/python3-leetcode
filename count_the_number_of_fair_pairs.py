from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()

        def worker(value: int) -> int:
            result = 0
            left = 0
            right = n - 1

            while left < right:
                sum = nums[left] + nums[right]
                if sum < value:
                    result += right - left
                    left += 1
                else:
                    right -= 1

            return result

        return worker(upper + 1) - worker(lower)
