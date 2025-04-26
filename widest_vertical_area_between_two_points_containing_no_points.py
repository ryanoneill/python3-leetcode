from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda point: point[0])
        result = max(points[i+1][0] - points[i][0] for i in range(n-1))

        return result
