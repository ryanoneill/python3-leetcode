from collections import defaultdict
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = defaultdict(int)
        for word in words:
            for letter in word:
                counts[letter] += 1

        n = len(words)
        result = True
        for count in counts.values():
            if count % n != 0:
                result = False
                break

        return result
