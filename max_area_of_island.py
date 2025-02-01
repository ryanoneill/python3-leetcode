from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0

        m = len(grid)
        n = len(grid[0])

        seen = set()
        for i in range(m):
            for j in range(n):
                value = grid[i][j]
                if value == 1:
                    current = 0
                    key = (i, j)

                    stack = []
                    seen.add(key)
                    stack.append(key)

                    while stack:
                        sq = stack.pop()
                        current += 1

                        # North
                        if sq[0] > 0:
                            north = (sq[0] - 1, sq[1])
                            if grid[north[0]][north[1]] == 1:
                                if north not in seen:
                                    seen.add(north)
                                    stack.append(north)

                        # South
                        if sq[0] < m-1:
                            south = (sq[0] + 1, sq[1])
                            if grid[south[0]][south[1]] == 1:
                                if south not in seen:
                                    seen.add(south)
                                    stack.append(south)

                        # East
                        if sq[1] < n-1:
                            east = (sq[0], sq[1] + 1)
                            if grid[east[0]][east[1]] == 1:
                                if not east in seen:
                                    seen.add(east)
                                    stack.append(east)

                        # West
                        if sq[1] > 0:
                            west = (sq[0], sq[1] - 1)
                            if grid[west[0]][west[1]] == 1:
                                if not west in seen:
                                    seen.add(west)
                                    stack.append(west)

                    result = max(result, current)

        return result
