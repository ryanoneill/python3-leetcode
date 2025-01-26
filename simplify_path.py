class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        segments = path.split("/")
        for segment in segments:
            if segment == "..":
                if stack:
                    stack.pop()
            elif segment != "" and segment != ".":
                stack.append(segment)
        result = "/" + "/".join(stack)
        return result
