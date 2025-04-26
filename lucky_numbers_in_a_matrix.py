from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        min_in_rows = [(100000, -1)] * m
        max_in_cols = [(0, -1)] * n

        for i in range(m):
            for j in range(n):
                num = matrix[i][j]
                if num < min_in_rows[i][0]:
                    min_in_rows[i] = (num, j)
                if num > max_in_cols[j][0]:
                    max_in_cols[j] = (num, i)


        result = []
        for num, col in min_in_rows:
            if max_in_cols[col][0] == num:
                result.append(num)

        return result

