from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = 0
        counter = Counter(tiles)

        def backtrack(counter: Counter) -> None:
            nonlocal result

            for key, value in counter.items():
                if value > 0:
                    result += 1
                    counter[key] -= 1
                    backtrack(counter)
                    counter[key] += 1

        backtrack(counter)

        return result
