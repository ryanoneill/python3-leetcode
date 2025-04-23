from is_subsequence import Solution

def test_ex1():
    s = "abc"
    t = "ahbgdc"
    solution = Solution()
    result = solution.isSubsequence(s, t)
    assert result

def test_ex2():
    s = "axc"
    t = "ahbgdc"
    solution = Solution()
    result = solution.isSubsequence(s, t)
    assert not result

