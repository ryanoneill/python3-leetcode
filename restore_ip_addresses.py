from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        n = len(s)

        def is_ok(previous: int, current: int) -> bool:
            result = True
            sub = s[previous:current]

            if sub[0] == "0" and len(sub) > 1:
                result = False
            elif int(sub) > 255:
                result = False

            return result

        def backtrack(places: List[int], start: int) -> None:
            if len(places) == 3:
                first = s[0 : places[0]]
                second = s[places[0] : places[1]]
                third = s[places[1] : places[2]]
                fourth = s[places[2] :]
                results.append(first + "." + second + "." + third + "." + fourth)
            else:
                for i in range(start, n):
                    previous = 0
                    if len(places) > 0:
                        previous = places[-1]
                    proceed = is_ok(previous, i)
                    if len(places) == 2:
                        proceed = proceed and is_ok(i, n)

                    if proceed:
                        places.append(i)
                        backtrack(places, i + 1)
                        places.pop()

        backtrack([], 1)

        return results
