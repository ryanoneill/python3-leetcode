from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        result = 0
        for i in range(n-2):
            j = i + 1
            k = i + 2

            sum = nums[i] + nums[k]
            if (2 * sum) == nums[j]:
                result += 1

        return result

