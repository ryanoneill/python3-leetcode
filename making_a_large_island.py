from typing import List


class Solution:
    def worker(self, grid: List[List[int]], marker: int, i: int, j: int) -> int:
        seen = set()
        result = 0

        m = len(grid)
        n = len(grid[0])

        key = (i, j)
        grid[i][j] = marker

        stack = []
        seen.add(key)
        stack.append(key)

        while stack:
            sq = stack.pop()
            result += 1

            # North
            if sq[0] > 0:
                north = (sq[0] - 1, sq[1])
                if grid[north[0]][north[1]] == 1:
                    if north not in seen:
                        grid[north[0]][north[1]] = marker
                        seen.add(north)
                        stack.append(north)

            # South
            if sq[0] < m - 1:
                south = (sq[0] + 1, sq[1])
                if grid[south[0]][south[1]] == 1:
                    if south not in seen:
                        grid[south[0]][south[1]] = marker
                        seen.add(south)
                        stack.append(south)

            # East
            if sq[1] < n - 1:
                east = (sq[0], sq[1] + 1)
                if grid[east[0]][east[1]] == 1:
                    if east not in seen:
                        grid[east[0]][east[1]] = marker
                        seen.add(east)
                        stack.append(east)

            # West
            if sq[1] > 0:
                west = (sq[0], sq[1] - 1)
                if grid[west[0]][west[1]] == 1:
                    if west not in seen:
                        grid[west[0]][west[1]] = marker
                        seen.add(west)
                        stack.append(west)

        return result

    def largestIsland(self, grid: List[List[int]]) -> int:
        result = 0

        m = len(grid)
        n = len(grid[0])

        areas = {}

        marker = 1

        for i in range(m):
            for j in range(n):
                value = grid[i][j]
                if value == 1:
                    marker += 1
                    area = self.worker(grid, marker, i, j)
                    areas[marker] = area

        if areas:
            result = max(areas.values())

        for i in range(m):
            for j in range(n):
                value = grid[i][j]
                if value == 0:
                    neighbors = set()

                    # North
                    if i > 0:
                        north = grid[i - 1][j]
                        if north != 0:
                            neighbors.add(north)

                    # South
                    if i < m - 1:
                        south = grid[i + 1][j]
                        if south != 0:
                            neighbors.add(south)

                    # East
                    if j < n - 1:
                        east = grid[i][j + 1]
                        if east != 0:
                            neighbors.add(east)

                    # West
                    if j > 0:
                        west = grid[i][j - 1]
                        if west != 0:
                            neighbors.add(west)

                    if len(neighbors) == 0:
                        result = max(1, result)
                    else:
                        current = 1
                        for neighbor in neighbors:
                            current += areas[neighbor]
                        result = max(current, result)

        return result
