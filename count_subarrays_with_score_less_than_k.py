from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0

        left = 0
        sum = 0
        width = 0
        score = 0
        for right, num in enumerate(nums):
            sum += num
            width = right - left + 1
            score = sum * width
            while score >= k:
                if left == right:
                    break
                else:
                    left_num = nums[left]
                    left += 1
                    sum -= left_num
                    width = right - left + 1
                    score = sum * width
            if score < k:
                result += width

        return result
