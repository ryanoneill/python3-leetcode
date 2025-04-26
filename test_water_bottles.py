from water_bottles import Solution

def test_ex1():
    numBottles = 9
    numExchange = 3
    solution = Solution()
    result = solution.numWaterBottles(numBottles, numExchange)
    assert result == 13

def test_ex2():
    numBottles = 15
    numExchanges = 4
    solution = Solution()
    result = solution.numWaterBottles(numBottles, numExchanges)
    assert result == 19
