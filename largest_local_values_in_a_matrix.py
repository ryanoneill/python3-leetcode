from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        result = [[0] * (n-2) for _ in range(m-2)]

        for i in range(2, m):
            for j in range(2, n):
                x = i - 2
                y = j - 2
                value = 0

                # upper left
                value = max(value, grid[i-2][j-2])
                # upper center
                value = max(value, grid[i-2][j-1])
                # upper right
                value = max(value, grid[i-2][j])
                # middle left
                value = max(value, grid[i-1][j-2])
                # middle center
                value = max(value, grid[i-1][j-1])
                # middle right
                value = max(value, grid[i-1][j])
                # bottom left
                value = max(value, grid[i][j-2])
                # bottom center
                value = max(value, grid[i][j-1])
                # bottom right
                value = max(value, grid[i][j])

                result[x][y] = value 

        return result


