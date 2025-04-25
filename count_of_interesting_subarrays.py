from collections import defaultdict
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        result = 0

        counts = defaultdict(int)
        counts[0] = 1
        prefix = 0

        for num in nums:
            if num % modulo == k:
                prefix += 1

            add_index = (prefix - k + modulo) % modulo
            result += counts[add_index]
            counts[prefix % modulo] += 1

        return result
