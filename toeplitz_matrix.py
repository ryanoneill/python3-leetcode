from typing import List


class Solution:
    def checkDiagonal(self, matrix: List[List[int]], row: int, col: int) -> bool:
        value = matrix[row][col]
        m = len(matrix)
        n = len(matrix[0])

        while row < m and col < n:
            row += 1
            col += 1

            if row < m and col < n:
                candidate = matrix[row][col]
                if candidate != value:
                    return False

        return True

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if not self.checkDiagonal(matrix, i, 0):
                return False

        for i in range(1, n):
            if not self.checkDiagonal(matrix, 0, i):
                return False

        return True
