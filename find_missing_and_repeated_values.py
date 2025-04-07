from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        actual = 0
        dupe = 0
        for row in grid:
            for value in row:
                if value in seen:
                    dupe = value
                else:
                    seen.add(value)
                    actual += value

        n = len(grid) * len(grid)
        expected = n * (n + 1) // 2
        missing = expected - actual
        return [dupe, missing]
