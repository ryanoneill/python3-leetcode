from score_of_a_string import Solution

def test_ex1():
    s = "hello"
    solution = Solution()
    result = solution.scoreOfString(s)
    assert result == 13

def test_ex2():
    s = "zaz"
    solution = Solution()
    result = solution.scoreOfString(s)
    assert result == 50
