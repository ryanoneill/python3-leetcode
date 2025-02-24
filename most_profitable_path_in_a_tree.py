from typing import List, Dict, Set

# Solution needs tons of work, but it passes
class Solution:
    def toAdjList(self, edges: List[List[int]]) -> Dict[int, Set[int]]:
        results = {}
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]

            if node1 not in results:
                results[node1] = set()
            results[node1].add(node2)
            if node2 not in results:
                results[node2] = set()
            results[node2].add(node1)
        return results

    def shortestPaths(self, adj_list: Dict[int, Set[int]], bob: int) -> Dict[int, List[int]]:
        results = {}
        seen = set()

        start = 0
        stack = [(start, [])]
        while stack:
            (current, path) = stack.pop()
            seen.add(current)
            path.append(current)
            n = len(adj_list[current])
            if n == 1 or current == bob:
                results[current] = path[:]
            for edge in adj_list[current]:
                if edge not in seen:
                    stack.append((edge, path[:]))

        return results

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj_list = self.toAdjList(edges)
        shortest_paths = self.shortestPaths(adj_list, bob)
        bob_path = list(reversed(shortest_paths[bob]))

        def runGame(dest: int) -> int:
            print("Run Game: " + str(dest))
            nonlocal adj_list
            nonlocal shortest_paths
            nonlocal bob_path
            nonlocal amount

            result = 0

            opened = set() 

            alice_path = shortest_paths[dest]
            alice_n = len(alice_path)
            bob_n = len(bob_path)

            alice_pos = -1
            bob_pos = -1

            for i in range(max(alice_n, bob_n)):
                if i < alice_n:
                    alice_pos = alice_path[i]
                if i < bob_n:
                    bob_pos = bob_path[i]

                if alice_pos == bob_pos:
                    if alice_pos not in opened:
                        result += amount[alice_pos] // 2
                        opened.add(alice_pos)
                else:
                    if alice_pos not in opened:
                        result += amount[alice_pos]
                        opened.add(alice_pos)
                    if bob_pos not in opened:
                        opened.add(bob_pos)

            return result

        # Bob's path is the shortest path from 0 -> bob reversed
        # What are the leafs? Edges is '1' and it's not '0'
        # Only run the game against the leafs
        result = -pow(2, 31)
        for key in adj_list:
            n = len(adj_list[key])
            if key != 0 and n == 1:
                value = runGame(key)
                result = max(result, value)

        return result
