class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)

        result = []

        k = max(m, n)

        for i in range(k):
            if i < m:
                result.append(word1[i])
            if i < n:
                result.append(word2[i])

        return "".join(result)
