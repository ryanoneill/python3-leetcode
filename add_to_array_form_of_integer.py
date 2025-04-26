from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        orig = list(num)
        orig[-1] += k
        carry = 0
        for i in reversed(range(n)):
            value = orig[i]
            value += carry
            carry, value = divmod(value, 10)
            orig[i] = value

        result = []
        while carry > 0:
            carry, value = divmod(carry, 10)
            result.append(value)

        result.reverse()
        result.extend(orig)

        return result
