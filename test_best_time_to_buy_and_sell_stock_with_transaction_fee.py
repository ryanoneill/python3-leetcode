from best_time_to_buy_and_sell_stock_with_transaction_fee import Solution

def test_ex1():
    prices = [1,3,2,8,4,9]
    fee = 2
    solution = Solution()
    result = solution.maxProfit(prices, fee)
    assert result == 8

def test_ex2():
    prices = [1,3,7,5,10,3]
    fee = 3
    solution = Solution()
    result = solution.maxProfit(prices, fee)
    assert result == 6
