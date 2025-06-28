from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        result = [(num, i) for i, num in enumerate(nums)]
        result = sorted(result, key=lambda item: item[0], reverse=True)[:k]
        result = sorted(result, key=lambda item: item[1])
        result = [item[0] for item in result]

        return result
