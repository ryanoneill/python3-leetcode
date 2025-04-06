from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = []

        def backtrack(subset: List[int], i: int):
            results.append(subset[:])
            for i in range(i, n):
                num = nums[i]
                subset.append(num)
                backtrack(subset, i+1)
                subset.pop()

        backtrack([], 0)

        return results
