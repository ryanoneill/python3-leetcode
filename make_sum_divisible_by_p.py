from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        result = n
        total = sum(nums)
        target = total % p
        seen = {}
        seen[0] = -1 

        if target == 0:
            result = 0
        else:
            current = 0
            for i, num in enumerate(nums):
                current += num
                modded = current % p
                seen[modded] = i

                diff = (current - target + p) % p
                if diff in seen:
                    result = min(result, i - seen[diff])

                seen[current] = i

        if result == n:
            result = -1

        return result
