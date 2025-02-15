from typing import Dict, Set

class Solution:
    def partitions(self, num: int, cache: Dict[int, Set[int]]) -> Set[int]:
        if num not in cache:
            results = {num}
            s = str(num)
            for j in range(1, len(s)):
                left = int(s[0:j])
                right = int(s[j:])
                inter = self.partitions(right, cache)
                for item in inter:
                    results.add(item + left)
            cache[num] = results
        return cache[num]

    def punishmentNumber(self, n: int) -> int:
        result = 0
        cache = {}
        for i in range(n+1):
            squared = i * i
            partitions = self.partitions(squared, cache)
            if i in partitions:
                result += squared

        return result
