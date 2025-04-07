class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for letter in s:
            if not stack:
                stack.append(letter)
            else:
                prior = stack[-1]
                if prior.islower():
                    value = prior.upper()
                    if value == letter:
                        stack.pop()
                    else:
                        stack.append(letter)
                else:
                    value = prior.lower()
                    if value == letter:
                        stack.pop()
                    else:
                        stack.append(letter)
        result = "".join(stack)
        return result
