from coin_change import Solution

def test_ex1():
    coins = [1,2,5]
    amount = 11
    solution = Solution()
    result = solution.coinChange(coins, amount)
    assert result == 3

def test_ex2():
    coins = [2]
    amount = 3
    solution = Solution()
    result = solution.coinChange(coins, amount)
    assert result == -1

def test_ex3():
    coins = [1]
    amount = 0
    solution = Solution()
    result = solution.coinChange(coins, amount)
    assert result == 0
