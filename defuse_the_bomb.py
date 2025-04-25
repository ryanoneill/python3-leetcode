from typing import List


class Solution:
    # TODO: Switch to use Sliding Window

    # code = [1,2,3,4,5,6]
    # prefix = [0,1,3,6,10,15,21]
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n

        if k != 0:
            prefix = [0] * (n + 1)
            total = 0

            for i in range(n):
                prefix[i] = total
                total += code[i]
            prefix[n] = total

            print(code)
            for i in range(n):
                if k > 0:
                    # replace i with the sum of the next k numbers
                    index = i + 1 + k
                    if index > n:
                        index -= n
                        result[i] = prefix[n] - prefix[i + 1]
                        result[i] += prefix[index] - prefix[0]
                    else:
                        result[i] = prefix[index] - prefix[i + 1]
                elif k < 0:
                    # replace i with the sum of the previous k numbers
                    index = i + k
                    if index < 0:
                        index += n
                        result[i] = prefix[n] - prefix[index]
                        result[i] += prefix[i] - prefix[0]
                    else:
                        result[i] = prefix[i] - prefix[index]

        return result
