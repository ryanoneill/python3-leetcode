from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]

        for i in range(n-2, -1, -1):
            points = questions[i][0]
            skip = questions[i][1]

            with_result = points
            if i + skip + 1 < n:
                with_result += dp[i + skip + 1]

            without_result = dp[i + 1]
            dp[i] = max(with_result, without_result)

        return dp[0]
