from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        result = False
        adj = {}
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            if node1 not in adj:
                adj[node1] = set()
            adj[node1].add(node2)
            if node2 not in adj:
                adj[node2] = set()
            adj[node2].add(node1)

        stack = []
        seen = set()

        if source == destination:
            result = True
        else:
            stack.append(source)
            seen.add(source)

        while stack:
            value = stack.pop()
            if value in adj:
                for edge in adj[value]:
                    if edge == destination:
                        result = True
                        break
                    if edge not in seen:
                        stack.append(edge)
                        seen.add(edge)

        return result

