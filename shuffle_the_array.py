from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for x, y in zip(range(n), range(n, 2*n)):
            result.append(nums[x])
            result.append(nums[y])

        return result

