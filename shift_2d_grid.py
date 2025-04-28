from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        n = rows * cols
        k %= n 

        if k == 0:
            results = grid
        else:
            results = [[0] * cols for _ in range(rows)]

            for i in range(rows):
                for j in range(cols):
                    previous = i * cols + j
                    current = (previous + k) % n
                    row, col = divmod(current, cols)
                    results[row][col] = grid[i][j]

        return results
