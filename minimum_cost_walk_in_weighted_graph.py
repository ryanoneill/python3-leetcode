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

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parents = list(range(n))

        for edge in edges:
            a = edge[0]
            b = edge[1]
            self.unite(parents, a, b)

        costs = {}
        for edge in edges:
            vertex = edge[0]
            parent = self.getParent(parents, vertex)
            cost = edge[2]
            if parent in costs:
                costs[parent] = costs[parent] & cost
            else:
                costs[parent] = cost

        results = []
        for q in query:
            a = q[0]
            b = q[1]
            apar = self.getParent(parents, a)
            bpar = self.getParent(parents, b)
            if apar != bpar:
                results.append(-1)
            else:
                results.append(costs[apar])

        return results
