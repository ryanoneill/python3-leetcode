from typing import List
from collections import deque
from heapq import heappush, heappop

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]):
        m = len(grid)
        n = len(grid[0])

        seen = set()
        queue = deque()

        k = len(queries)
        results = [0] * k

        heap = []
        for i, query in enumerate(queries):
            heappush(heap, (query, i))

        last = -1
        dead_ends = set()
        seen = set()
        while heap:
            queue = deque()
            query, index = heappop(heap)
            if last == -1:
                results[index] = 0

                position = (0, 0)
                seen.add(position)
                queue.append(position)
            elif queries[index] == queries[last]:
                results[index] = results[last]
            else:
                results[index] = results[last]
                for end in dead_ends:
                    queue.append(end)
                dead_ends = set()
            last = index

            while queue:
                i, j = queue.popleft()
                score = grid[i][j]

                if score >= query:
                    dead_ends.add((i, j))
                else:
                    results[index] += 1

                    if i > 0:
                        north = (i - 1, j)
                        if north not in seen:
                            seen.add(north)
                            queue.append(north)

                    if i < m - 1:
                        south = (i + 1, j)
                        if south not in seen:
                            seen.add(south)
                            queue.append(south)

                    if j > 0:
                        west = (i, j - 1)
                        if west not in seen:
                            seen.add(west)
                            queue.append(west)

                    if j < n - 1:
                        east = (i, j + 1)
                        if east not in seen:
                            seen.add(east)
                            queue.append(east)

        return results
