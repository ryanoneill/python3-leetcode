class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd_count = 0

        counts = {}
        for letter in s:
            if letter in counts:
                counts[letter] += 1
                if counts[letter] % 2 == 0:
                    odd_count -= 1
                else:
                    odd_count += 1
            else:
                counts[letter] = 1
                odd_count += 1

        return odd_count < 2
