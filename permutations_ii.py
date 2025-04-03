from typing import List, Set

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        n = len(nums)

        nums.sort()

        def backtrack(path: List[int], used: Set[int]) -> None:
            if len(path) == n:
                results.append(path[:])
            else:
                last = 10000 # range is -10 <= num <= 10
                for i in range(0, n):
                    value = nums[i]
                    if i not in used and value != last:
                        last = value
                        path.append(value)
                        used.add(i)
                        backtrack(path, used)
                        used.remove(i)
                        path.pop()

        backtrack([], set())
        return results

        

