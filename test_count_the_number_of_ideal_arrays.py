from count_the_number_of_ideal_arrays import Solution


def test_ex1():
    n = 2
    maxValue = 5
    solution = Solution()
    result = solution.idealArrays(n, maxValue)
    assert result == 10


def test_ex2():
    n = 5
    maxValue = 3
    solution = Solution()
    result = solution.idealArrays(n, maxValue)
    assert result == 11
