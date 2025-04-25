from count_and_say import Solution


def test_ex1():
    n = 4
    solution = Solution()
    result = solution.countAndSay(n)
    assert result == "1211"


def test_ex2():
    n = 1
    solution = Solution()
    result = solution.countAndSay(n)
    assert result == "1"


def test_ex3():
    n = 2
    solution = Solution()
    result = solution.countAndSay(n)
    assert result == "11"
