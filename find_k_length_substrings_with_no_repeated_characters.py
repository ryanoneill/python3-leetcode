class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        result = 0
        n = len(s)
        counts = {}

        for i in range(min(k, n)):
            letter = s[i]
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

        if len(counts) == k:
            result += 1

        for i in range(k, n):
            previous = s[i-k]
            counts[previous] -= 1
            if counts[previous] == 0:
                del counts[previous]
            letter = s[i]
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

            if len(counts) == k:
                result += 1

        return result
