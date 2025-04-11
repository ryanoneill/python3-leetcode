from typing import List

# TODO: Switch to use KMP or Rabin-Karp
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        results = []
        n = len(words)
        words.sort(key=lambda w: len(w))

        for i in range(n-1):
            for j in range(i+1, n):
                shorter = words[i]
                longer = words[j]
                pos = longer.find(shorter)
                if pos > -1:
                    results.append(shorter)
                    break

        return results
