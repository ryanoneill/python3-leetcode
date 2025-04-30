from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        result = 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        previous_row = [0] * n
        current_row = [0] * n

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    current_row[j] = 0
                elif i == 0 and j == 0:
                    current_row[j] = 1
                elif i == 0:
                    current_row[j] = current_row[j-1]
                elif j == 0:
                    current_row[j] = previous_row[j]
                else:
                    current_row[j] = previous_row[j] + current_row[j-1]
            result = current_row[n-1]
            previous_row, current_row = current_row, previous_row

        return result

