from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)

        result = len(seen) == 0
        return result
