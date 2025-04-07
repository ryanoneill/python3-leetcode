from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        values = []
        for row in grid:
            for num in row:
                values.append(num)

        values.sort()
        n = len(values)
        median = values[n // 2]
        moddian = median % x

        result = 0
        for value in values:
            if value % x != moddian:
                result = -1
                break
            else:
                result += abs(value - median) // x

        return result
