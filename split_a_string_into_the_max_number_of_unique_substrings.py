from typing import Set, Tuple

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)

        def worker(seen: Set[str], index: int) -> Tuple[bool, int]:
            result_bool = False
            result_count = 1

            if index == n:
                result_bool = True
                result_count = len(seen)
            else:
                for end in range(index+1, n+1):
                    sub = s[index:end]
                    if sub not in seen:
                        seen.add(sub)
                        cand_bool, cand_count = worker(seen, end)
                        if cand_bool:
                            result_bool = True
                            result_count = max(result_count, cand_count)
                        seen.remove(sub)

            return (result_bool, result_count)

        _, result = worker(set(), 0)
        return result
