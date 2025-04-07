from abc import abstractmethod


class Pattern:
    def __init__(self, value: str):
        self.value = value

    def matches_at(self, s: str, index: int) -> bool:
        result = False
        if self.value == ".":
            result = True
        else:
            result = s[index] == self.value
        return result

    @abstractmethod
    def is_multiple(self) -> bool:
        pass


class Single(Pattern):
    def is_multiple(self) -> bool:
        return False


class Multiple(Pattern):
    def is_multiple(self) -> bool:
        return True


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        patterns = []
        for i in range(len(p)):
            value = p[i]
            if value == "*":
                previous = patterns.pop()
                multiple = Multiple(previous.value)
                patterns.append(multiple)
            else:
                single = Single(value)
                patterns.append(single)

        cache = {}

        def worker(position: int, index: int) -> bool:
            nonlocal cache
            nonlocal patterns
            nonlocal s
            if index == len(s):
                if position == len(patterns):
                    return True
                else:
                    pattern = patterns[position]
                    if pattern.is_multiple():
                        return worker(position + 1, index)
                    else:
                        return False
            elif position == len(patterns):
                return False
            elif (position, index) in cache:
                return cache[(position, index)]
            else:
                pattern = patterns[position]
                if pattern.is_multiple():
                    result = pattern.matches_at(s, index)
                    if result:
                        result = worker(position, index + 1)
                        result = result or worker(position + 1, index + 1)
                        result = result or worker(position + 1, index)
                    else:
                        result = worker(position + 1, index)
                else:
                    result = pattern.matches_at(s, index)
                    if result:
                        result = worker(position + 1, index + 1)
                cache[(position, index)] = result
                return result

        return worker(0, 0)
