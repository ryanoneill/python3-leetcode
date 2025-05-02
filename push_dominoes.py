class Solution:
    # TODO: Improve this solution - slow
    def pushDominoes(self, dominoes: str) -> str:
        previous = dominoes
        current = ""

        n = len(previous)
        currents = [""] * n

        while True:
            left = "."
            right = "."
            for i, value in enumerate(previous):
                if value == "L" or value == "R":
                    currents[i] = value
                else:
                    if i-1 == -1:
                        left = "."
                    else:
                        left = previous[i-1]

                    if i+1 == n:
                        right = "."
                    else:
                        right = previous[i+1]

                    if left == "R" and right == "L":
                        value = "."
                    elif left == "R":
                        value = "R"
                    elif right == "L":
                        value = "L"

                    currents[i] = value
            current = "".join(currents)
            if current == previous:
                break
            else:
                previous = current

        return current
