class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for letter in s:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

        result = 0
        has_odd = False
        for value in counts.values():
            if value % 2 == 0:
                result += value
            else:
                has_odd = True
                result += value - 1

        if has_odd:
            result += 1
        return result
