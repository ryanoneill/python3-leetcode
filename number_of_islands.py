from typing import List, Set


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def worker(i: int, j: int, seen: Set["(int, int)"]):
            nonlocal grid
            nonlocal m
            nonlocal n

            seen.add((i, j))
            if grid[i][j] == "1":
                grid[i][j] = 0

                # North
                if i > 0:
                    if (i - 1, j) not in seen:
                        worker(i - 1, j, seen)

                # South
                if i < m - 1:
                    if (i + 1, j) not in seen:
                        worker(i + 1, j, seen)

                # East
                if j < n - 1:
                    if (i, j + 1) not in seen:
                        worker(i, j + 1, seen)

                # West
                if j > 0:
                    if (i, j - 1) not in seen:
                        worker(i, j - 1, seen)

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    result += 1
                    seen = set()
                    worker(i, j, seen)

        return result
