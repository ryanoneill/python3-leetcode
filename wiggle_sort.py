from typing import List

class Solution:
    def swap(self, nums: List[int], i: int, j: int) -> None:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)

        for i in range(n-1):
            num = nums[i]
            next = nums[i+1]

            if i % 2 == 0:
                if num > next:
                    self.swap(nums, i, i+1)
            else:
                if num < next:
                    self.swap(nums, i, i+1)
