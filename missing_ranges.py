from typing import List, Optional

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        results = []
        last: Optional[int] = None
        for num in nums:
            if last is not None:
                if last != num - 1:
                    range = [last + 1, num - 1]
                    results.append(range)
            else:
                if num > lower:
                    range = [lower, num - 1]
                    results.append(range)
            last = num
        if last is not None:
            if last < upper:
                range = [last+1, upper]
                results.append(range)
        else:
            range = [lower, upper]
            results.append(range)

        return results
