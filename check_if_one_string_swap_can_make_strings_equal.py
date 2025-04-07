class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 == n2:
            result = True
            diffs = []
            for i in range(n1):
                c1 = s1[i]
                c2 = s2[i]
                if c1 != c2:
                    diffs.append(i)
                    if len(diffs) > 2:
                        break

        d = len(diffs)
        if d == 0:
            result = True
        elif d == 1:
            result = False
        elif d == 2:
            i = diffs.pop()
            j = diffs.pop()
            result = s1[i] == s2[j] and s1[j] == s2[i]
        else:
            result = False

        return result
