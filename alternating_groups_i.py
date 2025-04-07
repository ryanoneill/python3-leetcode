from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        result = 0
        for i in range(n):
            first = colors[i % n]
            second = colors[(i + 1) % n]
            third = colors[(i + 2) % n]
            if first != second and second != third:
                result += 1
        return result
