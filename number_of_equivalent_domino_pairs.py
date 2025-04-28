from collections import Counter
from typing import List, Tuple
import math

class Solution:
    def domino_to_key(self, domino: List[int]) -> Tuple[int, int]:
        a, b = domino
        if b < a:
            a, b = b, a
        return (a, b)

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = Counter(map(self.domino_to_key, dominoes))
        result = sum(math.comb(count, 2) if count > 1 else 0 for count in counts.values())
        return result
