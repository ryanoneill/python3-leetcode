from regular_expression_matching import Solution


def test_ex1():
    s = "aa"
    p = "a"
    solution = Solution()
    result = solution.isMatch(s, p)
    assert not result


def test_ex2():
    s = "aa"
    p = "a*"
    solution = Solution()
    result = solution.isMatch(s, p)
    assert result


def test_ex3():
    s = "ab"
    p = ".*"
    solution = Solution()
    result = solution.isMatch(s, p)
    assert result


def test_ex4():
    s = "aab"
    p = "c*a*b"
    solution = Solution()
    result = solution.isMatch(s, p)
    assert result


def test_ex5():
    s = "mississippi"
    p = "mis*is*p*."
    solution = Solution()
    result = solution.isMatch(s, p)
    assert not result


def test_ex6():
    s = "a"
    p = "ab*"
    solution = Solution()
    result = solution.isMatch(s, p)
    assert result


def test_ex7():
    s = "bbbba"
    p = ".*a*a"
    solution = Solution()
    result = solution.isMatch(s, p)
    assert result
