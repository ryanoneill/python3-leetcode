from typing import List


# Using DFS on purpose as an exercise instead of UF
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            if node1 not in adj:
                adj[node1] = set()
            if node2 not in adj:
                adj[node2] = set()
            adj[node1].add(node2)
            adj[node2].add(node1)

        result = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                result += 1
                seen.add(i)
                stack = [i]

                while stack:
                    item = stack.pop()
                    if item in adj:
                        for edge in adj[item]:
                            if edge not in seen:
                                seen.add(edge)
                                stack.append(edge)

        return result
