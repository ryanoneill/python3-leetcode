from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        result = -1

        num1sum = 0
        num1zeros = 0
        for num in nums1:
            if num == 0:
                num1zeros += 1
            else:
                num1sum += num

        num2sum = 0
        num2zeros = 0
        for num in nums2:
            if num == 0:
                num2zeros += 1
            else:
                num2sum += num

        num1plus = num1sum + num1zeros
        num2plus = num2sum + num2zeros

        if num1plus == num2plus:
            result = num1plus
        elif num1plus > num2plus:
            if num2zeros != 0:
                result = num1plus
        else:
            if num1zeros != 0:
                result = num2plus

        return result


