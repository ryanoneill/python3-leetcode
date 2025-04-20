from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = {}
        for answer in answers:
            num = answer + 1
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        result = 0
        for num, count in counts.items():
            rem = count % num
            total = count - rem
            if rem > 0:
                total += num
            result += total

        return result
