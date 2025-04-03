from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []

        def backtrack(combination: List[int], start: int, remaining: int) -> None:
            if remaining == 0 and len(combination) == k:
                results.append(combination[:])
            elif remaining < 0 or len(combination) >= k:
                pass
            else:
                for value in range(start, 10):
                    combination.append(value)
                    backtrack(combination, value+1, remaining - value)
                    combination.pop()

        backtrack([], 1, n)

        return results
