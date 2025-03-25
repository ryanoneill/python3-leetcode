from heapq import heappush, heappop
from typing import List, Tuple

class Solution:
    def is_satisfied(self, recs: List[Tuple[int, int]]) -> bool:
        result = False

        current = 0
        count = 0
        while recs:
            start, end = heappop(recs)
            if current == 0:
                current = end
            elif start < current:
                current = max(current, end)
            else:
                count += 1
                if count == 2:
                    result = True
                    break
                current = end

        return result

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xs = []
        ys = []
        for rectangle in rectangles:
            start_x, start_y, end_x, end_y = rectangle
            heappush(xs, (start_x, end_x))
            heappush(ys, (start_y, end_y))

        result = self.is_satisfied(xs)
        result = result or self.is_satisfied(ys)

        return result
