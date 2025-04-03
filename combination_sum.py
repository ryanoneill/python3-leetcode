from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        results = []

        def backtrack(combination: List[int], start: int, remaining: int) -> None:
            if remaining == 0:
                results.append(combination[:])
            elif remaining < 0:
                pass
            else:
                for i in range(start, n):
                    value = candidates[i]
                    combination.append(value)
                    backtrack(combination, i, remaining - value)
                    combination.pop()

        backtrack([], 0, target)

        return results
