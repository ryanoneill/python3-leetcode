from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)

        result = 0
        # diagonal
        for i in range(m):
            result += mat[i][i]

        # anti-diagonal
        for i in range(m):
            j = m - 1 - i
            if i != j:
                result += mat[i][j]

        return result
