from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        result = True

        indexed = {letter: i for i, letter in enumerate(order)}

        last = words[0]
        last = list(map(lambda letter: indexed[letter], last))
        for i in range(1, n):
            current = words[i]
            current = list(map(lambda letter: indexed[letter], current))
            if last > current:
                result = False
                break
            else:
                last = current

        return result
