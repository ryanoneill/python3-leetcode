from typing import List

class Solution:
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        m = len(str1)
        n = len(str2)
        result = True

        if n < m:
            result = False
        elif n == m:
            result = str1 == str2
        else:
            result = str1 == str2[:m] and str1 == str2[n-m:]

        return result

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        result = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    result += 1
        return result
