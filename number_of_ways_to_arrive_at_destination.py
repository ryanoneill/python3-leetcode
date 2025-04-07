from typing import Dict, List
from heapq import heappush, heappop


class Solution:
    def adjacency(self, n: int, roads: List[List[int]]) -> Dict[int, Dict[int, int]]:
        result = {key: {} for key in range(n)}
        for road in roads:
            u, v, time = road
            result[u][v] = time
            result[v][u] = time
        return result

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = self.adjacency(n, roads)

        shortest_time = [float("inf")] * n
        shortest_path_counts = [0] * n

        heap = []
        heappush(heap, (0, 0))
        shortest_path_counts[0] = 1
        while heap:
            time_value, inter_value = heappop(heap)
            if time_value <= shortest_time[inter_value]:
                for inter_next, time_next in adj[inter_value].items():
                    combined = time_value + time_next
                    if combined < shortest_time[inter_next]:
                        shortest_time[inter_next] = combined
                        shortest_path_counts[inter_next] = shortest_path_counts[
                            inter_value
                        ]
                        heappush(heap, (combined, inter_next))
                    elif combined == shortest_time[inter_next]:
                        shortest_path_counts[inter_next] = (
                            shortest_path_counts[inter_next]
                            + shortest_path_counts[inter_value]
                        ) % 1000000007

        return shortest_path_counts[n - 1]
