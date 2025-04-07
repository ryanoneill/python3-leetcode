from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        posSum = 0
        currentPosSum = 0

        negSum = 0
        currentNegSum = 0
        for num in nums:
            if currentPosSum < 0:
                currentPosSum = num
            else:
                currentPosSum += num
            posSum = max(posSum, currentPosSum)

            if currentNegSum > 0:
                currentNegSum = num
            else:
                currentNegSum += num
            negSum = min(negSum, currentNegSum)

        return max(posSum, abs(negSum))
