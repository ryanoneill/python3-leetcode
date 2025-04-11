class Solution:
    def normalize(self, word: str) -> str:
        result = []
        for letter in word:
            if letter == "#":
                if result:
                    result.pop()
            else:
                result.append(letter)
        return "".join(result)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.normalize(s) == self.normalize(t)
