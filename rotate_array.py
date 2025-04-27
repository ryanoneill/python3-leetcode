from typing import List

class Solution:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


    def rotate(self, nums: List[int], k: int) -> None:
        # nums = [1,2,3,4,5,6,7], k = 3
        # ...
        # nums = [7,6,5,4,3,2,1]
        # nums = [5,6,7,4,3,2,1]
        # nums = [5,6,7,1,2,3,4]
        # ...
        # nums = [5,6,7,1,2,3,4]
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)

