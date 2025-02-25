from typing import List

class Solution:
    def compare(self, a: int, b: int) -> int:
        result = 0
        if a > b:
            result = -1
        elif a < b:
            result = 1
        else:
            result = 0
        return result
    
    def isMonotonic(self, nums: List[int]) -> bool:
        result = True

        n = len(nums)
        cmp = self.compare(nums[0], nums[n-1])
        last = nums[0]

        for i in range(1, n):
            num = nums[i]
            if cmp == 1:
                result = num >= last
            elif cmp == -1:
                result = num <= last
            else:
                result = num == last
            if not result:
                break
            last = num

        return result
