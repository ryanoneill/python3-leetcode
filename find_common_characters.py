from collections import Counter
from typing import List

class Solution:
    def merge(self, c: Counter, d: Counter) -> Counter:
        result = Counter()

        for key, value in c.items():
            if key in d:
                result[key] = min(value, d[key])

        return result

    def commonChars(self, words: List[str]) -> List[str]:
        previous = Counter(words[0])

        for word in words:
            current = Counter(word)
            previous = self.merge(previous, current)

        results = []
        for key, value in previous.items():
            for _ in range(value):
                results.append(key)

        return results
