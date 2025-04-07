from base_7 import Solution


def test_ex1():
    num = 100
    solution = Solution()
    result = solution.convertToBase7(num)
    assert result == "202"


def test_ex2():
    num = -7
    solution = Solution()
    result = solution.convertToBase7(num)
    assert result == "-10"


def test_ex3():
    num = 0
    solution = Solution()
    result = solution.convertToBase7(num)
    assert result == "0"
