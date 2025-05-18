from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        result = "none"

        valid = (nums[0] + nums[1]) > nums[2]
        valid = valid and (nums[0] + nums[2]) > nums[1]
        valid = valid and (nums[1] + nums[2]) > nums[0]

        if valid:
            sides = set(nums)
            match len(sides):
                case 1:
                    result = "equilateral"
                case 2:
                    result = "isosceles"
                case 3:
                    result = "scalene"
        return result
