from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        result = 0

        m = len(grid)
        n = len(grid[0])

        previous_row = [0] * n
        current_row = [0] * n

        for i in range(m):
            for j in range(n):
                value = grid[i][j]
                if i == 0 and j == 0:
                    current_row[j] = value
                elif i == 0:
                    current_row[j] = current_row[j-1] + value
                elif j == 0:
                    current_row[j] = previous_row[j] + value
                else:
                    current_row[j] = min(previous_row[j], current_row[j-1]) + value
            result = current_row[n-1]
            previous_row, current_row = current_row, previous_row

        return result
