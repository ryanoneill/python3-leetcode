from make_the_string_great import Solution


def test_ex1():
    s = "leEeetcode"
    solution = Solution()
    result = solution.makeGood(s)
    assert result == "leetcode"


def test_ex2():
    s = "abBAcC"
    solution = Solution()
    result = solution.makeGood(s)
    assert result == ""
