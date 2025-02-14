class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        result = 0
        left = 0
        n = len(s)

        counts = {}
        if k > 0:
            for right in range(n):
                letter = s[right]
                if letter in counts:
                    counts[letter] += 1
                else:
                    counts[letter] = 1
                distinct = len(counts)
                while distinct > k:
                    letter = s[left]
                    left += 1
                    counts[letter] -= 1
                    if counts[letter] == 0:
                        del counts[letter]
                    distinct = len(counts)
                current = right - left + 1
                result = max(result, current)

        return result
