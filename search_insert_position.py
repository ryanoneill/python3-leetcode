from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result = -1
        left = 0
        right = len(nums) - 1

        if target < nums[left]:
            result = 0
        elif target > nums[right]:
            result = right + 1
        else:
            while left <= right:
                mid = left + (right - left) // 2
                num = nums[mid]
                if num == target:
                    result = mid
                    break
                elif num < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    result = mid

        return result
