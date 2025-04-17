from collections import Counter
from heapq import heappop, heappush

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = []

        result = []

        for item in counter.items():
            letter, value = item
            heappush(heap, (-value, letter))

        last = ' '
        while heap:
            value, letter = heappop(heap)
            count = -value
            if letter == last:
                if heap:
                    alt_value, alt_letter = heappop(heap)
                    alt_count = -alt_value
                    last = alt_letter
                    result.append(alt_letter)
                    alt_count -= 1
                    if alt_count > 0:
                        heappush(heap, (-alt_count, alt_letter))
                else:
                    return ""
            else:
                count -= 1
                last = letter
                result.append(letter)
            if count > 0:
                heappush(heap, (-count, letter))

        return "".join(result)
