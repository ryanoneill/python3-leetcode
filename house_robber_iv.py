from typing import List

class Solution:
    def canRob(self, nums: List[int], k: int, amount: int) -> bool:
        result = False

        last = -1
        count = 0

        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num <= amount:
                if last == -1 or (i - last) != 1:
                    count += 1
                    last = i
            if count >= k:
                result = True
                break

        return result

    def minCapability(self, nums: List[int], k: int) -> int:
        right = max(nums)
        left = min(nums)

        result = right
        while left <= right:
            mid = left + (right - left) // 2
            if self.canRob(nums, k, mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
