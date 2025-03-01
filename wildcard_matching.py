class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def worker(position: int, index: int) -> bool:
            nonlocal cache
            result = False
            if index > len(s):
                result = False
            elif (position, index) in cache:
                result = cache[(position, index)]
            else:
                if position == len(p):
                    result = index == len(s)
                else:
                    pattern = p[position]
                    if pattern == "*":
                        result = result or worker(position, index+1)
                        result = result or worker(position+1, index+1)
                        result = result or worker(position+1, index)
                    elif index == len(s):
                        result = False
                    elif pattern == "?":
                        result = worker(position+1, index+1)
                    else:
                        result = pattern == s[index]
                        if result:
                            result = worker(position+1, index+1)
                cache[(position, index)] = result

            return result

        return worker(0, 0)
