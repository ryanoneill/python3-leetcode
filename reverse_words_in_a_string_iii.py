class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        words = s.split(" ")
        for word in words:
            result.append(word[::-1])
        return " ".join(result)
