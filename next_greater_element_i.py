from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next = {}

        for num in nums2:
            while stack:
                prev = stack[-1]
                if num > prev:
                    stack.pop()
                    next[prev] = num
                else:
                    break
            stack.append(num)
        stack.clear()

        result = []
        for num in nums1:
            if num in next:
                result.append(next[num])
            else:
                result.append(-1)

        return result


