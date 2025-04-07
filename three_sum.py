from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        last = None

        results = []
        n = len(nums)
        for i in range(n - 2):
            num = nums[i]
            if last != num:
                last = num
                diff = 0 - num
                left = i + 1
                right = n - 1

                while left < right:
                    sum = nums[left] + nums[right]
                    if sum == diff:
                        results.append([num, nums[left], nums[right]])
                        previous = nums[left]
                        while left < n and nums[left] == previous:
                            left += 1
                        right -= 1
                    elif sum < diff:
                        left += 1
                    else:
                        right -= 1

        return results
