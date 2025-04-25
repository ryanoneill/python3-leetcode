from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        result = ""
        counts = Counter(arr)

        j = 0
        for value in arr:
            if counts[value] == 1:
                j += 1
            if j == k:
                result = value
                break

        return result
