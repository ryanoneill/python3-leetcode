from collections import deque
from typing import List, Tuple

class Solution:
    def isClosed(self, grid: List[List[int]], key: Tuple[int, int]) -> bool:
        result = True

        m = len(grid)
        n = len(grid[0])
        
        queue = deque()
        queue.append(key)
        seen = set()
        seen.add(key)

        while queue:
            row, col = queue.popleft()
            grid[row][col] = 2

            # North
            if row > 0:
                north_row = row - 1
                north_col = col
                north = (north_row, north_col)
                if grid[north_row][north_col] == 0:
                    if north not in seen:
                        queue.append(north)
                        seen.add(north)
                        if north_row == 0:
                            result = False

            # South
            if row < m-1:
                south_row = row + 1
                south_col = col
                south = (south_row, south_col)
                if grid[south_row][south_col] == 0:
                    if south not in seen:
                        queue.append(south)
                        seen.add(south)
                        if south_row == m-1:
                            result = False

            # East
            if col < n-1:
                east_row = row
                east_col = col + 1
                east = (east_row, east_col)
                if grid[east_row][east_col] == 0:
                    if east not in seen:
                        queue.append(east)
                        seen.add(east)
                        if east_col == n-1:
                            result = False

            # West
            if col > 0:
                west_row = row
                west_col = col - 1
                west = (west_row, west_col)
                if grid[west_row][west_col] == 0:
                    if west not in seen:
                        queue.append(west)
                        seen.add(west)
                        if west_col == 0:
                            result = False

        return result

    def closedIsland(self, grid: List[List[int]]) -> int:
        result = 0

        m = len(grid)
        n = len(grid[0])
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 0:
                    key = (i, j)
                    if self.isClosed(grid, key):
                        result += 1

        return result
