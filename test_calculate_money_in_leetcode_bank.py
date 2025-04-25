from calculate_money_in_leetcode_bank import Solution


def test_ex1():
    n = 4
    solution = Solution()
    result = solution.totalMoney(n)
    assert result == 10


def test_ex2():
    n = 10
    solution = Solution()
    result = solution.totalMoney(n)
    assert result == 37


def test_ex3():
    n = 20
    solution = Solution()
    result = solution.totalMoney(n)
    assert result == 96
