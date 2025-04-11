class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        result = 0

        index = 0
        n = len(t)

        for letter in s:
            needle = t[index]
            if letter == needle:
                index += 1
            if index == n:
                break

        if index < n:
            result = n - index

        return result
