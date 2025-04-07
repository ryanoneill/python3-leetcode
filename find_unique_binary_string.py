from typing import List, Set


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def worker(items: List[str], index: int, n: int, seen: Set[str]) -> str:
            if index == n:
                candidate = "".join(items)
                if candidate in seen:
                    candidate = ""
                return candidate
            else:
                for digit in ["0", "1"]:
                    items.append(digit)
                    result = worker(items, index + 1, n, seen)
                    if result != "":
                        return result
                    else:
                        items.pop()
            return ""

        seen = set(nums)
        n = len(nums[0])
        result = worker([], 0, n, seen)
        return result
