from collections import deque
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        connected = {index: set() for index in range(n)}
        for edge in edges:
            vertex1, vertex2 = edge
            connected[vertex1].add(vertex2)
            connected[vertex2].add(vertex1)

        result = 0
        overall = set()
        for i in range(n):
            if i not in overall:
                seen = set()
                seen.add(i)
                queue = deque()
                queue.append(i)

                while queue:
                    item = queue.popleft()
                    for value in connected[item]:
                        if value not in seen:
                            seen.add(value)
                            queue.append(value)

                n = len(seen)
                should = True
                for item in seen:
                    if len(connected[item]) != n-1:
                        should = False
                        break

                if should:
                    result += 1

                overall = overall.union(seen)

        return result 
