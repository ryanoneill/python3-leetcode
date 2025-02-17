import copy
from typing import Dict, List

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def worker(counts: Dict[str, int], added: int, length: int) -> int:
            result = 0
            if added < length:
                for letter in counts:
                    result += 1
                    count = counts[letter]
                    left = copy.deepcopy(counts)
                    if count == 1:
                        del left[letter]
                    else:
                        left[letter] -= 1
                    result += worker(left, added+1, length)
            return result

        counts = {}
        n = len(tiles)
        for i in range(n):
            tile = tiles[i]
            if tile in counts:
                counts[tile] += 1
            else:
                counts[tile] = 1

        result = worker(counts, 0, n)

        return result
