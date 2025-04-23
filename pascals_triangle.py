from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        result.append([1])

        for i in range(1, numRows):
            result.append([])
            for j in range(0, i+1):
                if j == 0 or j == i:
                    result[i].append(1)
                else:
                    value = result[i-1][j] + result[i-1][j-1]
                    result[i].append(value)

        return result
