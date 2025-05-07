class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)[2:]
        result = True
        m = len(binary)
        last = binary[0]

        for i in range(1,m):
            digit = binary[i]
            if last == '0':
                result = digit == '1'
            else:
                result = digit == '0'
            if not result:
                break
            last = digit

        return result

