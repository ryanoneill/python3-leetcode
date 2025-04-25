from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        counts = Counter(chars)
        for word in words:
            n = len(word)
            current = Counter(word)
            word_result = True

            for key, value in current.items():
                if key not in counts:
                    word_result = False
                    break
                elif counts[key] < value:
                    word_result = False
                    break
            if word_result:
                result += n

        return result
