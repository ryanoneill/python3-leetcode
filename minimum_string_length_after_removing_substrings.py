class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for letter in s:
            if stack and letter == "B" and stack[-1] == "A":
                stack.pop()
            elif stack and letter == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(letter)

        return len(stack)
