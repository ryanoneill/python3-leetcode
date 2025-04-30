from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        results = []

        k = len(p)
        expected = Counter(p)

        actual = Counter()
        for letter in s[:k]:
            actual[letter] += 1

        if expected == actual:
            results.append(0)

        for left, letter in enumerate(s[k:]):
            previous = s[left]
            actual[previous] -= 1

            actual[letter] += 1
            if expected == actual:
                results.append(left+1)

        return results
