class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open = []
        closed = []

        for i, item in enumerate(s):
            if item == "(":
                open.append(i)
            elif item == ")":
                if open:
                    open.pop()
                else:
                    closed.append(i)

        bad = set(open).union(set(closed))
        result = []
        for i, item in enumerate(s):
            if i not in bad:
                result.append(item)

        return "".join(result)
