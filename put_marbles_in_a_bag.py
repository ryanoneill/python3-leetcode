from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        counts = k-1
        result = 0

        if counts > 0:
            split_pairs = [weights[i] + weights[i+1] for i in range(n-1)]
            split_pairs.sort()

            maximum = sum(split_pairs[-counts:])
            minimum = sum(split_pairs[:counts])
            difference = maximum - minimum
            result = difference

        return result

