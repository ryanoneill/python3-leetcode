class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        left = 0
        result = 0
        for right, letter in enumerate(s):
            if letter in letters:
                value = s[left]
                while value != letter:
                    letters.remove(value)
                    left += 1
                    value = s[left]
                letters.remove(value)
                left += 1
            letters.add(letter)
            current = right - left + 1
            result = max(result, current)
        return result
