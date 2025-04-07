from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        highest = arr[n - 1]
        nums = set(arr)

        result = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                current = 0
                first = arr[i]
                second = arr[j]
                sum = first + second
                if sum > highest:
                    break
                else:
                    while sum in nums:
                        if current == 0:
                            current = 3
                        else:
                            current += 1
                        first = second
                        second = sum
                        sum = first + second
                    result = max(result, current)

        return result
