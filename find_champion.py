from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        result = -1
        n = len(grid)

        for i in range(n):
            count = sum(grid[i])
            if count == n-1:
                result = i
                break

        return result
