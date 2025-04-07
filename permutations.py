from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        n = len(nums)

        def backtrack(path: List[int], used: Set[int]) -> None:
            if len(path) == n:
                results.append(path[:])
            else:
                for i in range(0, n):
                    if i not in used:
                        path.append(nums[i])
                        used.add(i)
                        backtrack(path, used)
                        used.remove(i)
                        path.pop()

        backtrack([], set())
        return results
