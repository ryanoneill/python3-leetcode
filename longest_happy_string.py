from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a != 0:
            heappush(heap, (-a, "a"))
        if b != 0:
            heappush(heap, (-b, "b"))
        if c != 0:
            heappush(heap, (-c, "c"))

        result = []
        hold = None
        while heap:
            negated, letter = heappop(heap)
            count = -negated
            result.append(letter)
            if hold:
                heappush(heap, hold)
                hold = None
            count -= 1
            if count > 0:
                if len(result) >= 2 and result[-1] == letter and result[-2] == letter:
                    hold = (-count, letter)
                else:
                    heappush(heap, (-count, letter))

        return "".join(result)
