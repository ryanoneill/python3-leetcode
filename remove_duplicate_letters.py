class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
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
                        if letter < peek and last[peek] > i:
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
