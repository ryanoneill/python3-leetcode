from count_the_number_of_fair_pairs import Solution


def test_ex1():
    nums = [0, 1, 7, 4, 4, 5]
    lower = 3
    upper = 6
    solution = Solution()
    result = solution.countFairPairs(nums, lower, upper)
    assert result == 6


def test_ex2():
    nums = [1, 7, 9, 2, 5]
    lower = 11
    upper = 11
    solution = Solution()
    result = solution.countFairPairs(nums, lower, upper)
    assert result == 1
