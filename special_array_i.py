from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        result = True
        n = len(nums)

        # odd = True, even = False
        last = nums[0] % 2 == 1
        for i in range(1, n):
            value = nums[i]
            current = value % 2 == 1
            result = last ^ current
            last = current
            if not result:
                break

        return result
