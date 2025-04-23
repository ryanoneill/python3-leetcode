class Solution:
    def countLargestGroup(self, n: int) -> int:
        maximum = 0
        result = 0
        counts = {}
        
        for i in range(1, n+1):
            value = str(i)
            total = sum(int(digit) for digit in value)
            if total in counts:
                counts[total] += 1
            else:
                counts[total] = 1
            current = counts[total]
            if current == maximum:
                result += 1
            elif current > maximum:
                maximum = current
                result = 1

        return result
