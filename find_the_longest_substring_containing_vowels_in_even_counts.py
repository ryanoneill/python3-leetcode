class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        result = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        value = 0
        seen = {}
        seen[value] = -1

        for i, letter in enumerate(s):
            if letter in vowels:
                value ^= ord(letter)

            if value in seen:
                result = max(result, i - seen[value])
            else:
                seen[value] = i

        return result



