from minimum_remove_to_make_valid_parentheses import Solution

def test_ex1():
    s = "lee(t(c)o)de)"
    solution = Solution()
    result = solution.minRemoveToMakeValid(s)
    assert result == "lee(t(c)o)de"

def test_ex2():
    s = "a)b(c)d"
    solution = Solution()
    result = solution.minRemoveToMakeValid(s)
    assert result == "ab(c)d"

def test_ex3():
    s = "))(("
    solution = Solution()
    result = solution.minRemoveToMakeValid(s)
    assert result == ""
