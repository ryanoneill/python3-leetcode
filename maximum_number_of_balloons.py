class Solution:
    def maxNumberOfBalloons(self, s: str) -> int:
        n = len(s)
        counts = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0,
        }
        for letter in s:
            if letter in counts:
                counts[letter] += 1
        counts['l'] = int(counts['l'] / 2)
        counts['o'] = int(counts['o'] / 2)
        result = n
        for value in counts.values():
            result = min(result, value)
        return result
