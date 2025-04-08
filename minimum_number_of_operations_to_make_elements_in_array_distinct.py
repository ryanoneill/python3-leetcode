from collections import Counter
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter(nums)
        dupes = set()
        for item, count in counter.items():
            if count > 1:
                dupes.add(item)

        index = 0
        result = 0
        while dupes:
            result += 1
            for i in range(index, min(index + 3, n)):
                num = nums[i]
                if num in dupes:
                    counter[num] -= 1
                    if counter[num] == 1:
                        dupes.remove(num)
            index += 3

        return result

