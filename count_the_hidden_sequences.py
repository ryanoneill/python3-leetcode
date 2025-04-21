from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # differences = [1, -3, 4], lower = 1, upper = 6
        n = len(differences) + 1
        prefix = [0] * n
        prefix[0] = 0

        # prefix = [0, 1, -2, 2]

        for i, diff in enumerate(differences):
            prefix[i] = prefix[i-1] + diff

        # min_offset = -2
        # max_offset = 2

        min_offset = min(prefix)
        max_offset = max(prefix)

        # lower_bound = 1 - -2 = 3
        # upper_bound = 6 - 2 = 4

        lower_bound = lower - min_offset
        upper_bound = upper - max_offset 

        if upper_bound >= lower_bound:
            result = upper_bound - lower_bound + 1
        else:
            result = 0

        return result


