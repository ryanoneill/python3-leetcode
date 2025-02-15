class Solution:
    def countLetters(self, s: str) -> int:
        last = ''
        run = 0
        result = 0

        for letter in s:
            if letter == last:
                run += 1
            else:
                last = letter
                run = 1

            result += run

        return result


