class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {}
        for i, letter in enumerate(s):
            last[letter] = i

        stack = []
        seen = set()
        for i, letter in enumerate(s):
            if letter not in seen:
                while True:
                    if stack:
                        peek = stack[-1]
                        if letter < peek and i < last[peek]:
                            stack.pop()
                            seen.remove(peek)
                        else:
                            break
                    else:
                        break
                stack.append(letter)
                seen.add(letter)

        result = "".join(stack)
        return result
