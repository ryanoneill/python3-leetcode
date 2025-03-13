from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        sum = 0
        for i in range(n):
            sum += nums[i]
            nums[i] = sum

        m = len(queries)
        results = [0] * m

        for i in range(m):
            query = queries[i]

            left = 0
            right = n - 1

            result = 0
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == query:
                    result = mid + 1
                    break
                elif nums[mid] < query:
                    left = mid + 1
                    result = mid + 1
                else:
                    right = mid - 1

            results[i] = result

        return results

