from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1 for _ in range(n)]
        
        stack = []
        for i, num in enumerate(nums):
            while stack:
                peek_index = stack[-1]
                peek_num = nums[peek_index]
                if num > peek_num:
                    result[peek_index] = num
                    stack.pop()
                else:
                    break
            stack.append(i)

        for num in nums:
            while stack:
                peek_index = stack[-1]
                peek_num = nums[peek_index]
                if num > peek_num:
                    result[peek_index] = num
                    stack.pop()
                else:
                    break

        return result
