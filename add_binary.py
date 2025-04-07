class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_n = len(a)
        b_n = len(b)

        carry = False
        result = []
        for index in range(max(a_n, b_n)):
            a_value = "0"
            b_value = "0"

            if index < a_n:
                a_value = a[a_n - index - 1]
            if index < b_n:
                b_value = b[b_n - index - 1]

            sum = ""
            if a_value == "1" and b_value == "1":
                sum = "0"
                if carry:
                    sum = "1"
                carry = True
            elif a_value == "1" and b_value == "0":
                sum = "1"
                if carry:
                    sum = "0"
            elif a_value == "0" and b_value == "1":
                sum = "1"
                if carry:
                    sum = "0"
            else:
                sum = "0"
                if carry:
                    sum = "1"
                    carry = False

            result.append(sum)
        if carry:
            result.append("1")

        return "".join(reversed(result))
