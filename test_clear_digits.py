from clear_digits import Solution

def test_ex1():
    s = "abc"
    solution = Solution()
    result = solution.clearDigits(s)
    assert result == "abc"

def test_ex2():
    s = "cb34"
    solution = Solution()
    result = solution.clearDigits(s)
    assert result == ""
