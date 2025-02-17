from typing import Dict, List

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def worker(keys: List[str], counts: Dict[str, int], added: int, length: int) -> int:
            result = 0
            if added < length:
                for letter in keys:
                    count = counts[letter]
                    if count > 0:
                        result += 1
                        counts[letter] -= 1
                        result += worker(keys, counts, added+1, length)
                        counts[letter] += 1
            return result

        counts = {}
        n = len(tiles)
        for i in range(n):
            tile = tiles[i]
            if tile in counts:
                counts[tile] += 1
            else:
                counts[tile] = 1
        keys = []
        for key in counts:
            keys.append(key)

        result = worker(keys, counts, 0, n)

        return result
