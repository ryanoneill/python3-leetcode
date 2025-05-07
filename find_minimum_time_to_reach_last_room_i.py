from heapq import heappush, heappop
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        minTime = [[-1] * m for _ in range(n)]

        heap = []
        heappush(heap, (0, 0, 0))

        while heap:
            cost, row, col = heappop(heap)
            previous = minTime[row][col]
            if previous == -1 or cost < previous:
                minTime[row][col] = cost

                # North
                if row > 0:
                    north_row = row-1
                    north_col = col
                    north_cost = max(moveTime[north_row][north_col], cost) + 1

                    north_previous = minTime[north_row][north_col]
                    if north_previous == -1 or north_cost < north_previous:
                        heappush(heap, (north_cost, north_row, north_col))

                # South
                if row < n-1:
                    south_row = row+1
                    south_col = col
                    south_cost = max(moveTime[south_row][south_col], cost) + 1

                    south_previous = minTime[south_row][south_col]
                    if south_previous == -1 or south_cost < south_previous:
                        heappush(heap, (south_cost, south_row, south_col))

                # East
                if col < m-1:
                    east_row = row
                    east_col = col+1
                    east_cost = max(moveTime[east_row][east_col], cost) + 1

                    east_previous = minTime[east_row][east_col]
                    if east_previous == -1 or east_cost < east_previous:
                        heappush(heap, (east_cost, east_row, east_col))

                # West
                if col > 0:
                    west_row = row
                    west_col = col-1
                    west_cost = max(moveTime[west_row][west_col], cost) + 1

                    west_previous = minTime[west_row][west_col]
                    if west_previous == -1 or west_cost < west_previous:
                        heappush(heap, (west_cost, west_row, west_col))

        return minTime[n-1][m-1]
