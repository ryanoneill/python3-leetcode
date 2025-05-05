from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []

        n = len(nums)
        queue = deque()

        for i in range(k):
            num = nums[i]
            while queue and num > queue[-1][0]:
                queue.pop()
            queue.append((num, i))

        results.append(queue[0][0])
        for i in range(k, n):
            if queue:
                peek_index = queue[0][1]
                if peek_index <= i - k:
                    queue.popleft()

            num = nums[i]
            while queue and num > queue[-1][0]:
                queue.pop()
            queue.append((num, i))
            results.append(queue[0][0])
            
        return results
