class Solution:
    def isSatisfied(self, counts: dict) -> bool:
        return counts["a"] > 0 and counts["b"] > 0 and counts["c"] > 0

    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        counts = {"a": 0, "b": 0, "c": 0}
        left = 0
        right = 0
        result = 0

        left = 0
        for right, letter in enumerate(s):
            counts[letter] += 1
            while self.isSatisfied(counts):
                result += n - right
                previous = s[left]
                counts[previous] -= 1
                left += 1

        return result
