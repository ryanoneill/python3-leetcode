from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        results = []

        last = -1
        for word, group in zip(words, groups):
            if group != last:
                results.append(word)
                last = group

        return results
