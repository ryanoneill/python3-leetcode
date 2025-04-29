from collections import deque
from typing import Deque, List, Tuple

class Solution:
    def updateDistances(
        self,
        grid: List[List[int]],
        queue: Deque[Tuple[int, int]]
    ) -> None:
        n = len(grid)
        total = n * n

        seen = set()

        moves = 0
        while queue:
            k = len(queue)
            for _ in range(k):
                row, col = queue.popleft()
                grid[row][col] = min(moves, grid[row][col])

                # North
                if row > 0:
                    north_row, north_col = row - 1, col
                    north = (north_row, north_col)
                    if north not in seen and grid[north_row][north_col] == total:
                        queue.append(north)
                        seen.add(north)

                # South
                if row < n-1:
                    south_row, south_col = row + 1, col
                    south = (south_row, south_col)
                    if south not in seen and grid[south_row][south_col] == total:
                        queue.append(south)
                        seen.add(south)

                # East
                if col < n-1:
                    east_row, east_col = row, col + 1
                    east = (east_row, east_col)
                    if east not in seen and grid[east_row][east_col] == total:
                        queue.append(east)
                        seen.add(east)

                # West
                if col > 0:
                    west_row, west_col = row, col - 1
                    west = (west_row, west_col)
                    if west not in seen and grid[west_row][west_col] == total:
                        queue.append(west)
                        seen.add(west)

            moves += 1

    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        total = n * n

        has_land = False
        has_water = False

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    has_land = True
                else:
                    grid[i][j] = total
                    has_water = True


        result = -1
        if has_land and has_water:
            queue = deque()
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 0:
                        key = (i, j)
                        queue.append(key)

            self.updateDistances(grid, queue)
            for i in range(n):
                for j in range(n):
                    result = max(result, grid[i][j])

        return result
