class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        sn = len(s)
        sint = int(s)

        def count(value: int) -> int:
            if sint > value:
                return 0

            digits = str(value)
            n = len(digits)
            prefixn = n - sn

            cache = {}
            def worker(i: int, tight: bool) -> int:
                key = (i, tight)
                if i == n:
                    return 1
                elif key in cache:
                    return cache[key]
                else:
                    result = 0
                    digit_max = int(digits[i]) if tight else 9
                    if i < prefixn:
                        for digit in range(min(digit_max, limit) + 1):
                            still_tight = tight and digit == digit_max
                            result += worker(i + 1, still_tight)
                    else:
                        digit = int(s[i - prefixn])
                        if digit <= min(digit_max, limit):
                            still_tight = tight and digit == digit_max
                            result = worker(i + 1, still_tight)

                    cache[key] = result
                    return result

            return worker(0, True)

        return count(finish) - count(start-1)
