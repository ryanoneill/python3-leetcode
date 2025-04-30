from typing import List, Tuple

class Solution:
    def isSubIsland(self, grid1: List[List[int]], grid2: List[List[int]], key: Tuple[int, int]) -> bool:
        result = True

        m = len(grid1)
        n = len(grid1[0])

        stack = []
        stack.append(key)
        seen = set()
        seen.add(key)

        while stack:
            row, col = stack.pop()
            if grid1[row][col] != 1:
                result = False
            grid2[row][col] = 2

            # North
            if row > 0:
                north_row, north_col = row - 1, col
                north = (north_row, north_col)
                if north not in seen and grid2[north_row][north_col] == 1:
                    stack.append(north)
                    seen.add(north)

            # South
            if row < m-1:
                south_row, south_col = row + 1, col
                south = (south_row, south_col)
                if south not in seen and grid2[south_row][south_col] == 1:
                    stack.append(south)
                    seen.add(south)

            # East
            if col < n-1:
                east_row, east_col = row, col + 1
                east = (east_row, east_col)
                if east not in seen and grid2[east_row][east_col] == 1:
                    stack.append(east)
                    seen.add(east)

            # West
            if col > 0:
                west_row, west_col = row, col - 1
                west = (west_row, west_col)
                if west not in seen and grid2[west_row][west_col] == 1:
                    stack.append(west)
                    seen.add(west)

        return result

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        result = 0
        m = len(grid1)
        n = len(grid1[0])

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    key = (i, j)
                    if self.isSubIsland(grid1, grid2, key):
                        result += 1

        return result
