from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.v1_n = len(v1)
        self.v2_n = len(v2)
        self.first = self.v1_n > 0
        self.index = 0

    def next(self) -> int:
        result = -1
        if self.first:
            result = self.v1[self.index]
            if self.index < self.v2_n:
                self.first = False
            else:
                self.index += 1
        else:
            result = self.v2[self.index]
            self.index += 1
            if self.index < self.v1_n:
                self.first = True
        return result

    def hasNext(self) -> bool:
        result = False
        if self.first:
            result = self.index < self.v1_n
        else:
            result = self.index < self.v2_n
        return result
