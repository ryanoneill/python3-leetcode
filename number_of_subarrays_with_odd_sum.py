from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        result = 0

        sum = 0

        odds = 0
        evens = 1

        for num in arr:
            sum += num
            if sum % 2 == 1:
                result += evens
                odds += 1
            else:
                result += odds
                evens += 1

            result %= 10**9 + 7

        return result
