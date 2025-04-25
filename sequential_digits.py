from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_n = len(str(low))
        high_n = len(str(high))

        options = []
        for i in range(low_n, high_n + 1):
            for j in range(1, 10 - i + 1):
                value = [str(k) for k in range(j, j + i)]
                option = int("".join(value))
                if low <= option <= high:
                    options.append(option)

        return options
