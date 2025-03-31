from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Uses CycleSort
        result = []
        n = len(nums)
        for i in range(n):
            while nums[i] != i + 1:
                value = nums[i]
                index = value - 1
                if nums[index] == value:
                    break
                else:
                    nums[i], nums[index] = nums[index], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                result.append(nums[i])
            
        return result

