from buy_two_chocolates import Solution

def test_ex1():
    prices = [1,2,2]
    money = 3
    solution = Solution()
    result = solution.buyChoco(prices, money)
    assert result == 0

def test_ex2():
    prices = [3,2,3]
    money = 3
    solution = Solution()
    result = solution.buyChoco(prices, money)
    assert result == 3
