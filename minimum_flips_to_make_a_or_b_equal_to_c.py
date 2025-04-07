class Solution:
    def make_bin(self, value: int, n: int) -> str:
        result = bin(value)[2:]
        diff = n - len(result)
        result = ("0" * diff) + result
        return result

    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0
        maximum = bin(10**9)[2:]
        n = len(maximum)

        bin_a = self.make_bin(a, n)
        bin_b = self.make_bin(b, n)
        bin_c = self.make_bin(c, n)

        for i in range(n):
            bit_a = bin_a[i]
            bit_b = bin_b[i]
            bit_c = bin_c[i]

            if bit_c == "0":
                if bit_a != "0":
                    result += 1
                if bit_b != "0":
                    result += 1
            else:
                if bit_a == "0" and bit_b == "0":
                    result += 1

        return result
