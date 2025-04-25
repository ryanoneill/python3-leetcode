from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                square = grid[i][j]
                if square == 1:
                    # North
                    if i == 0 or grid[i - 1][j] == 0:
                        result += 1

                    # South
                    if i == m - 1 or grid[i + 1][j] == 0:
                        result += 1

                    # East
                    if j == n - 1 or grid[i][j + 1] == 0:
                        result += 1

                    # West
                    if j == 0 or grid[i][j - 1] == 0:
                        result += 1

        return result
