class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        if m == 0:
            return n
        elif n == 0:
            return m
        else:
            dp = [[0] * (n + 1) for _ in range(m + 1)]

            for i in range(1, m + 1):
                dp[i][0] = i
            for j in range(1, n + 1):
                dp[0][j] = j
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    l1 = word1[i - 1]
                    l2 = word2[j - 1]
                    if l1 == l2:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        option1 = dp[i - 1][j]
                        option2 = dp[i - 1][j - 1]
                        option3 = dp[i][j - 1]
                        dp[i][j] = 1 + min(option1, option2, option3)

            return dp[m][n]
