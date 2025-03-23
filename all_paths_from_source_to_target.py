from collections import deque
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        results = []
        queue = deque()
        queue.append((0, [0]))
        while queue:
            item, path = queue.popleft()
            if item == n-1:
                results.append(path)
            else:
                for next in graph[item]:
                    next_path = path[:]
                    next_path.append(next)
                    queue.append((next, next_path))
        return results
