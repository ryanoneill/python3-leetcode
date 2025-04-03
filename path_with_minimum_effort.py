from heapq import heappush, heappop
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        columns = len(heights[0])

        efforts = [[10_000_000] * columns for _ in range(rows)]

        heap = []
        heappush(heap, (0, (0, 0)))
        while heap:
            effort, position = heappop(heap)
            row, col = position
            previous = efforts[row][col]
            if effort < previous:
                efforts[row][col] = effort
                height = heights[row][col]

                for x, y in [(0,-1), (0,1), (-1,0), (1,0)]:
                    new_row = row + x
                    new_col = col + y

                    if 0 <= new_row < rows and 0 <= new_col < columns:
                        new_height = heights[new_row][new_col]
                        diff = max(effort, abs(new_height - height))
                        heappush(heap, (diff, (new_row, new_col)))

        return efforts[rows-1][columns-1]

