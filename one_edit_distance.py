class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        result = False

        ns = len(s)
        nt = len(t)

        if ns > nt:
            result = self.isOneEditDistance(t, s)
        elif nt - ns > 1:
            result = False
        else:
            used = False
            for i in range(ns):
                cs = s[i]
                ct = t[i]

                if cs != ct:
                    used = True
                    if ns == nt:
                        result = s[i+1:] == t[i+1:]
                        break
                    else:
                        result = s[i:] == t[i+1:]
                        break

            if not used:
                result = nt - ns == 1

        return result
