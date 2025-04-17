from collections import Counter
from heapq import heappop, heappush, heapify

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = []

        result = []

        heap = [(-value, letter) for letter, value in counter.items()]
        heapify(heap)

        while heap:
            value, letter = heappop(heap)
            count = -value
            if result and letter == result[-1]:
                if heap:
                    alt_value, alt_letter = heappop(heap)
                    alt_count = -alt_value
                    result.append(alt_letter)
                    alt_count -= 1
                    if alt_count > 0:
                        heappush(heap, (-alt_count, alt_letter))
                else:
                    return ""
            else:
                count -= 1
                result.append(letter)
            if count > 0:
                heappush(heap, (-count, letter))

        return "".join(result)
