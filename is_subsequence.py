class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sn = len(s)

        index_s = 0
        if sn > 0:
            for letter in t:
                if s[index_s] == letter:
                    index_s += 1
                    if index_s == sn:
                        break

        return index_s == sn
