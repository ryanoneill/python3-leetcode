from find_the_difference import Solution

def test_ex1():
    s = "abcd"
    t = "abcde"
    solution = Solution()
    result = solution.findTheDifference(s, t)
    assert result == "e"

def test_ex2():
    s = ""
    t = "y"
    solution = Solution()
    result = solution.findTheDifference(s, t)
    assert result == "y"


