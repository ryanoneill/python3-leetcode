from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            match log:
                case "./":
                    pass
                case "../":
                    if stack:
                        stack.pop()
                case _:
                    stack.append(log)

        return len(stack)
