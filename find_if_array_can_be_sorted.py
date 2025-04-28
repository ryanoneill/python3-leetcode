from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        result = True
        n = len(nums)

        for i in range(1,n):
            previous = nums[i-1]
            current = nums[i]
            if previous > current:
                if previous.bit_count() == current.bit_count():
                    nums[i-1], nums[i] = current, previous
                else:
                    result = False
                    break

        if result:
            for j in reversed(range(1,n)):
                previous = nums[j-1]
                current = nums[j]
                if previous > current:
                    if previous.bit_count() == current.bit_count():
                        nums[j-1], nums[j] = current, previous
                    else:
                        result = False
                        break

        return result
