from wildcard_matching import Solution

def test_ex1():
    s = "aa"
    p = "a"
    solution = Solution()
    result = solution.isMatch(s, p)
    assert not result

def test_ex2():
    s = "aa"
    p = "*"
    solution = Solution()
    result = solution.isMatch(s, p)
    assert result

def test_ex3():
    s = "cb"
    p = "?a"
    solution = Solution()
    result = solution.isMatch(s, p)
    assert not result

def test_ex4():
    s = ""
    p = "*"
    solution = Solution()
    result = solution.isMatch(s, p)
    assert result

def test_ex5():
    s = "acdcb"
    p = "a*c?b"
    solution = Solution()
    result = solution.isMatch(s, p)
    assert not result
