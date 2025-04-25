from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result = []
        freq1 = Counter(s1.split(" "))
        freq2 = Counter(s2.split(" "))

        for word, value in freq1.items():
            if value == 1 and word not in freq2:
                result.append(word)

        for word, value in freq2.items():
            if value == 1 and word not in freq1:
                result.append(word)

        return result
