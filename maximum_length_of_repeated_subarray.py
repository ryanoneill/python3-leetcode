from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        m = len(nums1)
        n = len(nums2)

        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                num1 = nums1[i]
                num2 = nums2[j]
                if num1 == num2:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    result = max(result, dp[i][j])

        return result
