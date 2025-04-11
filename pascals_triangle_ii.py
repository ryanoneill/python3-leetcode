from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex
        row = [1]
        for k in range(1, n + 1):
            value = (row[-1] * (n - k + 1) // k)
            row.append(value)

        return row
