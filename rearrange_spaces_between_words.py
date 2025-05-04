class Solution:
    def reorderSpaces(self, text: str) -> str:
        original = len(text)
        parts = [part for part in text.split(" ") if len(part) > 0]
        current = sum([len(item) for item in parts])
        diff = original - current
        n = len(parts)

        result = ""
        if n == 1:
            spaces = diff
        else:
            spaces = diff // (n - 1)
        for i, part in enumerate(parts):
            result += part
            if i < n-1:
                result += " " * spaces
                diff -= spaces
            else:
                result += " " * diff

        return result
