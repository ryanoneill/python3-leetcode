from lemonade_change import Solution


def test_ex1():
    bills = [5, 5, 5, 10, 20]
    solution = Solution()
    result = solution.lemonadeChange(bills)
    assert result


def test_ex2():
    bills = [5, 5, 10, 10, 20]
    solution = Solution()
    result = solution.lemonadeChange(bills)
    assert not result
