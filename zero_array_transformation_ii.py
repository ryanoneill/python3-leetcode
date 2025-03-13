from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        m = len(queries)
        result = -1

        if self.becomes_zero_array(nums, queries, m):
            left = 0
            right = m

            while left <= right:
                mid = left + (right - left) // 2
                if self.becomes_zero_array(nums, queries, mid):
                    right = mid - 1
                else:
                    left = mid + 1

            result = left

        return result

    def becomes_zero_array(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        result = True

        n = len(nums)
        sum = 0
        diffs = [0] * (n + 1)

        for i in range(k):
            left, right, value = queries[i]
            diffs[left] += value
            diffs[right+1] -= value

        for i in range(n):
            sum += diffs[i]
            if sum < nums[i]:
                result = False
                break

        return result
