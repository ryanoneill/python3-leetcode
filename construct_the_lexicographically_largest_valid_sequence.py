from typing import List


class Solution:
    def worker(self, items: List[int], remain: List[int]) -> (bool, List[int]):
        if not remain:
            return (True, items)
        else:
            for i in range(len(remain)):
                value = remain[i]
                these = items[:]
                left = [x for x in remain if x != value]
                first = these.index(0)
                these[first] = value
                if value == 1:
                    return self.worker(these, left)
                else:
                    second = first + value
                    if second < len(these) and these[second] == 0:
                        these[second] = value
                        (result, response) = self.worker(these, left)
                        if result:
                            return (result, response)
        return (False, [])

    def constructDistancedSequence(self, n: int) -> List[int]:
        length = (n - 1) * 2 + 1
        items = [0 for i in range(length)]
        remain = [i for i in range(n, 0, -1)]

        (result, value) = self.worker(items, remain)

        return value

    # n = 1, result = [1]
    # n = 2, result = [2, 1, 2]
    # n = 3, result = [3, 1, 2, 3, 2]
    # n = 4, result = [4, 2, 3, 2, 4, 3, 1]
    # n = 5, result = [5, 3, 1, 4, 3, 5, 2, 4, 2]

    # For every integer i between 2 and n, the distance between the
    # two occurrences of i is exactly i

    # 1 must occur once
    # 2 must occur twice
    # 3 must occur twice
