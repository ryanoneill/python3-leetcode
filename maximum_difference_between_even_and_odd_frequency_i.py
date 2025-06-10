from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)

        max_odd = 0
        min_even = len(s)

        for count in counts.values():
            if count % 2 == 1:
                max_odd = max(max_odd, count)
            else:
                min_even = min(min_even, count)

        result = max_odd - min_even

        return result
