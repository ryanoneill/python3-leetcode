from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(key=lambda x: -x)
        s.sort(key=lambda x: -x)

        g_n = len(g)
        s_n = len(s)

        g_index = 0
        s_index = 0

        result = 0
        while g_index < g_n and s_index < s_n:
            greed = g[g_index]
            size = s[s_index]
            if size >= greed:
                result += 1
                s_index += 1
            g_index += 1

        return result
            


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content_children = 0
        cookie_index = 0
        while cookie_index < len(s) and content_children < len(g):
            if s[cookie_index] >= g[content_children]:
                content_children += 1
            cookie_index += 1
        return content_children
