from typing import List


# TODO: Implement CompressedSparseRow
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat2)
        n = len(mat2[0])

        result = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for x in range(k):
                m1value = mat1[i][x]
                if m1value != 0:
                    for j in range(n):
                        result[i][j] += m1value * mat2[x][j]

        return result
