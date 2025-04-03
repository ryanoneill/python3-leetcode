from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        results = []

        def backtrack(combination: List[int], start: int, remaining: int) -> None:
            if remaining == 0:
                results.append(combination[:])
            elif remaining < 0:
                pass
            else:
                last = -1
                for i in range(start, n):
                    value = candidates[i]
                    if value != last:
                        last = value
                        next_remaining = remaining - value
                        if next_remaining < 0:
                            break
                        combination.append(value)
                        backtrack(combination, i+1, next_remaining)
                        combination.pop()

        backtrack([], 0, target)

        return results
