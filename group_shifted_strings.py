from typing import List

class Solution:
    def key(self, s: str) -> str:
        result = []
        base = ord(s[0])
        for letter in s:
            value = (ord(letter) - base + 26) % 26
            result.append(chr(value + ord('a')))
        return "".join(result)

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        results = []
        hash = {}
        for s in strings:
            key = self.key(s)
            if key in hash:
                hash[key].append(s)
            else:
                hash[key] = [s]

        for key in hash:
            results.append(hash[key])

        return results

