from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        letters = sorted(s, key = lambda letter: (-counter[letter], letter))
        result = "".join(letters)
        return result
