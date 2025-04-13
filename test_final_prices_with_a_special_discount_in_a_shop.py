from final_prices_with_a_special_discount_in_a_shop import Solution

def test_ex1():
    prices = [8,4,6,2,3]
    solution = Solution()
    result = solution.finalPrices(prices)
    assert result == [4,2,4,2,3]

def test_ex2():
    prices = [1,2,3,4,5]
    solution = Solution()
    result = solution.finalPrices(prices)
    assert result == [1,2,3,4,5]

def test_ex3():
    prices = [10,1,1,6]
    solution = Solution()
    result = solution.finalPrices(prices)
    assert result == [9,0,1,6]
