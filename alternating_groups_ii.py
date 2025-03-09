from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        count = 0
        last = -1
        n = len(colors)
        result = 0

        for i in range(n + k - 1):
            j = i % n
            color = colors[j]
            if color != last:
                count += 1
            else:
                count = 1
            if count >= k:
                result += 1
            last = color

        return result
