from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        result = 0
        counter = Counter(s)
        for value in counter.values():
            if value % 2 == 1:
                result += 1
            else:
                result += 2

        return result
