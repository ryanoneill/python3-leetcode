class Solution:
    # TODO: Switch to using Knuth-Morris-Pratt
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)

        stack = []
        for letter in s:
            stack.append(letter)
            if letter == part[-1]:
                m = len(stack)
                if m > n-1:
                    matches = True
                    for i in range(n):
                        s_index = m - n + i
                        if stack[s_index] != part[i]:
                            matches = False
                            break
                    if matches:
                        for i in range(n):
                            stack.pop()

        return "".join(stack)


