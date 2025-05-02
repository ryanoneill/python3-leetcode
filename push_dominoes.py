class Solution:
    # Performance:
    # 1st iteration: Beats  5% (LOL)
    # 2nd iteration: Beats  5% (LOL - But Faster)
    # 3rd iteration: Beats 82% (Much Better and Unique)
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        results = ["."] * n

        stack = []
        for i, domino in enumerate(dominoes):
            results[i] = domino
            if not stack:
                stack.append(i)
            elif domino == "R":
                peek_index = stack[-1]
                peek = dominoes[peek_index]
                if peek == "R":
                    for j in range(peek_index+1, i):
                        results[j] = "R"
                stack.pop()
                stack.append(i)
            elif domino == "L":
                peek_index = stack[-1]
                peek = dominoes[peek_index]
                if peek == "L":
                    for j in range(peek_index+1, i):
                        results[j] = "L"
                elif peek == ".":
                    for j in range(peek_index, i):
                        results[j] = "L"
                else:
                    left = peek_index + 1
                    right = i - 1
                    while left < right:
                        results[left] = "R"
                        results[right] = "L"
                        left += 1
                        right -= 1
                stack.pop()

        if stack:
            peek_index = stack[-1]
            peek = dominoes[peek_index]
            if peek == "R":
                for j in range(peek_index, n):
                    results[j] = "R"

        return "".join(results)
