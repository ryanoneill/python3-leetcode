from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window = 0
        for num in data:
            if num == 1:
                window += 1

        count = 0
        for i in range(window):
            if data[i] == 1:
                count += 1

        n = len(data)
        result = window - count
        for j in range(window, n):
            if data[j - window] == 1:
                count -= 1
            if data[j] == 1:
                count += 1
            result = min(result, window - count)

        return result
