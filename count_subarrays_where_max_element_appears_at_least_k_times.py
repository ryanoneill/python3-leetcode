from collections import deque
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        max_value = -1
        positions = deque()

        for i, num in enumerate(nums):
            if num > max_value:
                max_value = num
                positions = deque()
                positions.append(i)
                result = 0
            elif num == max_value:
                positions.append(i)
                if len(positions) > k:
                    positions.popleft()

            if len(positions) == k:
                head = positions[0]
                result += head + 1

        return result
