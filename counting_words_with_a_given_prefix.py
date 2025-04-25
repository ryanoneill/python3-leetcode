from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        result = 0
        for word in words:
            m = len(word)
            if m >= n:
                if word[:n] == pref:
                    result += 1

        return result
