from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        results = []

        line = []
        width = 0
        for word in words:
            m = len(word)
            padding = len(line) - 1
            if padding + m + width >= maxWidth:
                k = len(line)
                if k == 1:
                    result = line[0] + (" " * (maxWidth - width))
                    results.append(result)
                else:
                    remain = maxWidth - width
                    spaces, plus = divmod(remain, k-1)
                    result = line[0]
                    for i in range(1, k):
                        if plus > 0:
                            result += " " * (spaces + 1)
                            plus -= 1
                        else:
                            result += " " * spaces
                        result += line[i]
                    results.append(result)
                line = []
                width = 0
            width += m
            line.append(word)

        result = " ".join(line)
        result += " " * (maxWidth - len(result))

        results.append(result)

        return results
