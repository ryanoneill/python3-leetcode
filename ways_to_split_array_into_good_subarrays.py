from typing import List

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        result = 0

        last = -1
        for i, num in enumerate(nums):
            if num == 1:
                if last == -1:
                    result = 1
                else:
                    diff = i - last
                    result = result * diff % MOD
                last = i

        return result



