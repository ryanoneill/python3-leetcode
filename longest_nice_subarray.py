from typing import List
from collections import deque

# TODO: There is no need for a queue here. Simple sliding window
# is sufficient.
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        result = 0
        current = deque()

        for num in nums:
            i = len(current) - 1 
            while i > -1 and current[i] & num == 0:
                i -= 1

            while i != -1:
                current.popleft()
                i -= 1

            current.append(num)

            result = max(result, len(current))

        return result

