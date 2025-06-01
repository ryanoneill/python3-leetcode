from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row = False
        first_col = False

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                value = matrix[i][j]
                if value == 0:
                    if i == 0:
                        first_row = True
                    else:
                        matrix[i][0] = 0
                    if j == 0:
                        first_col = True
                    else:
                        matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        if first_row:
            for j in range(n):
                matrix[0][j] = 0

        if first_col:
            for i in range(m):
                matrix[i][0] = 0
