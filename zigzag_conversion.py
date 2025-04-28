class Solution:
    def convert(self, s: str, numRows: int) -> str:
        results = [[] for _ in range(numRows)]

        i = 0
        direction_down = True
        for letter in s:
            results[i].append(letter)
            if numRows > 1:
                if i == 0:
                    direction_down = True
                elif i == numRows-1:
                    direction_down = False

                if direction_down:
                    i += 1
                else:
                    i -= 1

        result = "".join(map(lambda x: "".join(x), results))
        return result

