from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        chars = set(allowed)

        for word in words:
            add = True
            for letter in word:
                if letter not in chars:
                    add = False
                    break

            if add:
                result += 1

        return result
