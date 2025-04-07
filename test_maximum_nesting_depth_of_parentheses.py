from maximum_nesting_depth_of_parentheses import Solution


def test_ex1():
    s = "(1+(2*3)+((8)/4))+1"
    solution = Solution()
    result = solution.maxDepth(s)
    assert result == 3


def test_ex2():
    s = "(1)+((2))+(((3)))"
    solution = Solution()
    result = solution.maxDepth(s)
    assert result == 3


def test_ex3():
    s = "()(())((()()))"
    solution = Solution()
    result = solution.maxDepth(s)
    assert result == 3
