from number_of_dice_rolls_with_target_sum import Solution

def test_ex1():
    n = 1
    k = 6
    target = 3
    solution = Solution()
    result = solution.numRollsToTarget(n, k, target)
    assert result == 1

def test_ex2():
    n = 2
    k = 6
    target = 7
    solution = Solution()
    result = solution.numRollsToTarget(n, k, target)
    assert result == 6

def test_ex3():
    n = 30
    k = 30
    target = 500
    solution = Solution()
    result = solution.numRollsToTarget(n, k, target)
    assert result == 222616187

def test_ex4():
    n = 20
    k = 15
    target = 987
    solution = Solution()
    result = solution.numRollsToTarget(n, k, target)
    assert result == 0
