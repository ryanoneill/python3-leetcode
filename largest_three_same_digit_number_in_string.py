class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result_int = -1
        last = -1
        start = -1

        for i, value in enumerate(num):
            if i == 0 or value != last:
                last = value
                start = i
            elif i == start + 2:
                value_int = int(value)
                if value_int > result_int:
                    result_int = value_int

        if result_int == -1:
            result = ""
        else:
            result = str(result_int) * 3

        return result
