class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        value = columnNumber - 1
        while value >= 0:
            digit = value % 26
            letter = chr(ord("A") + digit)
            result.append(letter)
            value = (value // 26) - 1
        return "".join(reversed(result))
