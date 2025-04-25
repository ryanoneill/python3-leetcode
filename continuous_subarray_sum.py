from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        result = False
        current = 0
        seen = {}
        seen[0] = -1

        for i, num in enumerate(nums):
            current = (current + num) % k

            if current in seen:
                previous = seen[current]
                result = (i - previous) >= 2
                if result:
                    break
            else:
                seen[current] = i

        return result
