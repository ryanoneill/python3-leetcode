from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        result = 0
        n = len(nums)
        indices = {}
        for i in range(n):
            num = nums[i]
            if num in indices:
                for j in indices[num]:
                    mult = i * j
                    if mult % k == 0:
                        result += 1
                indices[num].add(i)
            else:
                indices[num] = {i}

        return result
