from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_max = 0
        current_min = 0

        maximum_sum = nums[0] 
        minimum_sum = nums[0]

        total_sum = 0

        for num in nums:
            current_max = max(num, current_max + num)
            current_min = min(num, current_min + num)

            maximum_sum = max(maximum_sum, current_max)
            minimum_sum = min(minimum_sum, current_min)

            total_sum += num

        result = maximum_sum 
        if total_sum != minimum_sum:
            result = max(result, total_sum - minimum_sum)

        return result

