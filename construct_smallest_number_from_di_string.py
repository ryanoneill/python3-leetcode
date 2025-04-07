class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern) + 1

        used = [False for _ in range(n)]
        current = [0 for _ in range(n)]

        def worker(last: int, index: int) -> bool:
            result = True
            if index < n:
                for i in range(n):
                    if not used[i]:
                        value = i + 1
                        can_proceed = last == 0
                        can_proceed = can_proceed or (
                            pattern[index - 1] == "I" and value > last
                        )
                        can_proceed = can_proceed or (
                            pattern[index - 1] == "D" and value < last
                        )
                        if can_proceed:
                            current[index] = value
                            used[i] = True
                            result = worker(value, index + 1)
                            if result:
                                return True
                            else:
                                current[index] = 0
                                used[i] = False
                        else:
                            result = False

            return result

        worker(0, 0)

        return "".join(map(str, current))
