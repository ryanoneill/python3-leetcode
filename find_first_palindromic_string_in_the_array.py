from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True

        n = len(s)
        mid = n // 2
        if n % 2 == 0: # 6, we want left to be 2 and right to be 3
            left = mid - 1
            right = mid
        else:          # 7, we want left to be 2 and right to be 4
            left = mid - 1
            right = mid + 1

        for _ in range(mid):
            a = s[left]
            b = s[right]
            if a == b:
                left -= 1
                right += 1
            else:
                result = False
                break

        return result

    def firstPalindrome(self, words: List[str]) -> str:
        result = ""
        for word in words:
            if self.isPalindrome(word):
                result = word
                break

        return result


