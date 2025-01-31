from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = { "a", "e", "i", "o", "u" }
        prefix = [0]
        sum = 0
        for word in words:
            begin = word[0] in vowels
            end = word[-1] in vowels
            if begin and end:
                sum += 1
            prefix.append(sum)

        result = []
        for query in queries:
            left = query[0]
            right = query[1]
            value = prefix[right+1] - prefix[left]
            result.append(value)

        return result

