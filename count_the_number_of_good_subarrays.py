from collections import Counter
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counts = Counter()
        result = 0

        pairs = 0
        left = 0

        for right, num in enumerate(nums):
            pairs += counts[num]
            counts[num] += 1

            while pairs >= k:
                result += n - right
                left_num = nums[left]
                counts[left_num] -= 1
                pairs -= counts[left_num]
                left += 1

        return result
