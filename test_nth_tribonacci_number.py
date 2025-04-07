from nth_tribonacci_number import Solution


def test_ex1():
    n = 4
    solution = Solution()
    result = solution.tribonacci(n)
    assert result == 4


def test_ex2():
    n = 25
    solution = Solution()
    result = solution.tribonacci(n)
    assert result == 1389537
