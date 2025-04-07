from best_time_to_buy_and_sell_stock import Solution


def test_ex1():
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    result = solution.maxProfit(prices)
    assert result == 5


def test_ex2():
    prices = [7, 6, 4, 3, 1]
    solution = Solution()
    result = solution.maxProfit(prices)
    assert result == 0
