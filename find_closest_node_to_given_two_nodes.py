from collections import deque
from typing import List

class Solution:
    def findDistances(self, edges: List[int], node: int) -> List[int]:
        n = len(edges)

        result = [-1 for _ in range(n)]

        queue = deque()
        queue.append((0, node))
        seen = set()
        seen.add(node)

        while queue:
            distance, index = queue.popleft()
            if result[index] == -1:
                result[index] = distance

            next_node = edges[index]
            if next_node != -1 and next_node not in seen:
                queue.append((distance + 1, next_node))
                seen.add(next_node)

        return result

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        node1d = self.findDistances(edges, node1)
        node2d = self.findDistances(edges, node2)

        resultd = -1
        resulti = -1
        for i, distances in enumerate(zip(node1d, node2d)):
            d1, d2 = distances
            if d1 != -1 and d2 != -1:
                max_away = max(d1, d2)
                if resultd == -1:
                    resultd = max_away
                    resulti = i
                elif max_away < resultd:
                    resultd = max_away
                    resulti = i

        return resulti
