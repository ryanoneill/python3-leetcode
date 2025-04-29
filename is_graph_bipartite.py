from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        colors = [0 for _ in range(n)]
        # 0 is no color
        # 1 is blue
        # 2 is red

        seen = set()
        queue = deque()

        result = True
        for i in range(n):
            if i not in seen:
                seen.add(i)
                queue.append(i)

            while queue:
                i = queue.popleft()
                for j in graph[i]:
                    if j not in seen:
                        seen.add(j)
                        queue.append(j)

                    if colors[i] == 0:
                        if colors[j] == 0:
                            colors[i] = 1
                            colors[j] = 2
                        elif colors[j] == 1:
                            colors[i] = 2
                        else:
                            colors[i] = 1
                    elif colors[i] == 1:
                        if colors[j] == 0:
                            colors[j] = 2
                        elif colors[j] == 1:
                            result = False
                            break
                    else:
                        if colors[j] == 0:
                            colors[j] = 1
                        elif colors[j] == 2:
                            result = False
                            break

        return result


