from coin_change_ii import Solution

def test_ex1():
    amount = 5
    coins = [1,2,5]
    solution = Solution()
    result = solution.change(amount, coins)
    assert result == 4

def test_ex2():
    amount = 3
    coins = [2]
    solution = Solution()
    result = solution.change(amount, coins)
    assert result == 0

def test_ex3():
    amount = 10
    coins = [10]
    solution = Solution()
    result = solution.change(amount, coins)
    assert result == 1

