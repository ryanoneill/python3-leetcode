from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        result = True
        count = 0

        n = len(nums)
        previous = nums[0]
        for i in range(1, n):
            num = nums[i]
            if num < previous:
                count += 1
                if count > 1:
                    result = False
                    break
            previous = num

        if result and count == 1:
            result = nums[-1] <= nums[0]

        return result
