from collections import Counter
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        counts = Counter(nums)
        (dominant, total) = counts.most_common(1)[0]

        seen = 0
        result = -1
        left = total
        for index, num in enumerate(nums):
            if num == dominant:
                seen += 1
                left = total - seen

            other_left = (index + 1) - seen
            other_right = (n - index - 1) - left
            if seen > other_left and left > other_right:
                result = index
                break

        return result
