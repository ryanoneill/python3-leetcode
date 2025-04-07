from house_robber import Solution


def test_ex1():
    nums = [1, 2, 3, 1]
    solution = Solution()
    result = solution.rob(nums)
    assert result == 4


def test_ex2():
    nums = [2, 7, 9, 3, 1]
    solution = Solution()
    result = solution.rob(nums)
    assert result == 12


def test_ex3():
    nums = [5]
    solution = Solution()
    result = solution.rob(nums)
    assert result == 5
