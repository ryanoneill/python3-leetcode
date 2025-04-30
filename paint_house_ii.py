from typing import List
import heapq

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])

        previous_row = [0] * k
        current_row = [0] * k

        for i in range(n):
            cost = costs[i]
            min1, min2 = heapq.nsmallest(2, enumerate(previous_row), key=lambda x: x[1])
            for j in range(k):
                if i == 0:
                    current_row[j] = cost[j]
                elif j == min1[0]:
                    current_row[j] = min2[1] + cost[j]
                else:
                    current_row[j] = min1[1] + cost[j]
            previous_row, current_row = current_row, previous_row

        return min(previous_row)
