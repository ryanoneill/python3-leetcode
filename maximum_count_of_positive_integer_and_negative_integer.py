from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n - 1
        pos_index = n

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid - 1
                pos_index = mid

        left = 0
        right = n - 1
        neg_index = n

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1
                neg_index = mid

        positive = n - pos_index
        negative = neg_index
        result = max(positive, negative)

        return result
