from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        result = True

        n = len(hand)

        groups, rem = divmod(n, groupSize)
        if rem != 0:
            result = False
        else:
            counts = Counter(hand)

            for _ in range(groups):
                minimum = min(counts.keys())
                for num in range(minimum, minimum + groupSize):
                    if counts[num]:
                        counts[num] -= 1
                        if counts[num] == 0:
                            del counts[num]
                    else:
                        result = False
                        break
                if not result:
                    break

        return result
