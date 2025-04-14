from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        n = len(target)
        counts = [0] * 1001
        for i in range(n):
            counts[target[i]] += 1
            counts[arr[i]] -= 1

        result = True
        for i in range(1001):
            if counts[i] != 0:
                result = False
                break
        return result
