class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            s = self.countAndSay(n-1)
            result = []
            last = ''
            count = 0
            for value in s:
                if value == last:
                    count += 1
                else:
                    if last != "":
                        result.append(str(count))
                        result.append(last)
                    last = value
                    count = 1

            result.append(str(count))
            result.append(last)

            return "".join(result)

