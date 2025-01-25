from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        result = 0
        counts = {}
        for num in arr:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for num in counts:
            next = num + 1
            if next in counts:
                result += counts[num]
        return result
