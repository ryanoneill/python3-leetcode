from collections import deque
from typing import List, Tuple

class Solution:
    def hasFish(self, grid: List[List[int]], key: Tuple[int, int]) -> bool:
        row, col = key
        return grid[row][col] > 0

    def grabFish(self, grid: List[List[int]], key: Tuple[int, int]) -> int:
        m = len(grid)
        n = len(grid[0])

        result = 0
        queue = deque()
        queue.append(key)
        seen = set()
        seen.add(key)
        while queue:
            row, col = queue.popleft()
            result += grid[row][col]
            grid[row][col] = 0
            
            # North
            if row > 0:
                north = (row-1, col)
                if north not in seen and self.hasFish(grid, north):
                    seen.add(north)
                    queue.append(north)

            # South
            if row < m-1:
                south = (row+1, col)
                if south not in seen and self.hasFish(grid, south):
                    seen.add(south)
                    queue.append(south)

            # East
            if col < n-1:
                east = (row, col+1)
                if east not in seen and self.hasFish(grid, east):
                    seen.add(east)
                    queue.append(east)

            # West
            if col > 0:
                west = (row, col-1)
                if west not in seen and self.hasFish(grid, west):
                    seen.add(west)
                    queue.append(west)

        return result

    def findMaxFish(self, grid: List[List[int]]) -> int:
        result = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    attempt = self.grabFish(grid, (i, j))
                    result = max(result, attempt)

        return result
