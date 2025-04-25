from backspace_string_compare import Solution


def test_ex1():
    s = "ab#c"
    t = "ad#c"
    solution = Solution()
    result = solution.backspaceCompare(s, t)
    assert result


def test_ex2():
    s = "ab##"
    t = "c#d#"
    solution = Solution()
    result = solution.backspaceCompare(s, t)
    assert result


def test_ex3():
    s = "a#c"
    t = "b"
    solution = Solution()
    result = solution.backspaceCompare(s, t)
    assert not result
