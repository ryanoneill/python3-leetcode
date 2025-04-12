class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        result = -1
        first = {}
        for i, letter in enumerate(s):
            if letter in first:
                current = i - first[letter] - 1
                result = max(result, current)
            else:
                first[letter] = i

        return result


