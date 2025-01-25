from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sum = 0
        sums = [0]
        for num in nums:
            sum += num
            sums.append(sum)
        result = []
        for i in range(n):
            if i < k:
                result.append(-1)
            elif n - k <= i:
                result.append(-1)
            else:
                sum = sums[i+k+1] - sums[i-k]
                divisor = 2 * k + 1
                value = int(sum / divisor)
                result.append(value)
        return result
