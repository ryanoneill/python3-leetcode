from count_good_numbers import Solution


def test_ex1():
    n = 1
    solution = Solution()
    result = solution.countGoodNumbers(n)
    assert result == 5


def test_ex2():
    n = 4
    solution = Solution()
    result = solution.countGoodNumbers(n)
    assert result == 400


def test_ex3():
    n = 50
    solution = Solution()
    result = solution.countGoodNumbers(n)
    assert result == 564908303


def test_ex4():
    n = 10**15
    solution = Solution()
    result = solution.countGoodNumbers(n)
    assert result == 711414395


def test_ex5():
    n = 806166225460393
    solution = Solution()
    result = solution.countGoodNumbers(n)
    assert result == 643535977
