from collections import Counter
from typing import List

class Solution:
    def getParent(self, parents: List[int], i: int) -> int:
        if parents[i] == i:
            return i
        else:
            result = self.getParent(parents, parents[i])
            parents[i] = result
            return result


    def unite(self, parents: List[int], i: int, j: int) -> None:
        ipar = self.getParent(parents, i)
        jpar = self.getParent(parents, j)
        parents[jpar] = ipar


    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        total = m * n
        parents = [i for i in range(total)]

        by_column = {}

        for row in range(m):
            last_in_row = -1
            for col in range(n):
                index = row * n + col
                value = grid[row][col]
                if value == 1:
                    if last_in_row != -1:
                        self.unite(parents, index, last_in_row)
                    last_in_row = index
                    if col in by_column:
                        last_in_col = by_column[col]
                        self.unite(parents, index, last_in_col)
                    by_column[col] = index

        for i in range(total):
            self.getParent(parents, i)

        counter = Counter(parents)
        print(parents)
        result = sum(value if value > 1 else 0 for value in counter.values())
        return result
