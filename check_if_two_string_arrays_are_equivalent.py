from itertools import zip_longest
from typing import Iterator, List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def gen(words: List[str]) -> Iterator[str]:
            for word in words:
                for letter in word:
                    yield letter

        word1_gen = gen(word1)
        word2_gen = gen(word2)

        result = True
        for l1, l2 in zip_longest(word1_gen, word2_gen):
            if l1 is None or l2 is None or l1 != l2:
                result = False
                break

        return result
