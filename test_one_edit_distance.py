from one_edit_distance import Solution

def test_ex1():
    s = "ab"
    t = "acb"
    solution = Solution()
    result = solution.isOneEditDistance(s, t)
    assert result

def test_ex2():
    s = ""
    t = ""
    solution = Solution()
    result = solution.isOneEditDistance(s, t)
    assert not result

def test_ex3():
    s = ""
    t = "a"
    solution = Solution()
    result = solution.isOneEditDistance(s, t)
    assert result

def test_ex4():
    s = "a"
    t = "A"
    solution = Solution()
    result = solution.isOneEditDistance(s, t)
    assert result

def test_ex5():
    s = "accb"
    t = "acb"
    solution = Solution()
    result = solution.isOneEditDistance(s, t)
    assert result
