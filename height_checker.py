from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        result = 0
        counts = [0 for _ in range(101)]
        for height in heights:
            counts[height] += 1

        expected = []
        for i, count in enumerate(counts):
            if count > 0:
                for _ in range(count):
                    expected.append(i)

        for actual, expect in zip(heights, expected):
            if actual != expect:
                result += 1

        return result
