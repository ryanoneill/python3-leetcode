from number_of_good_pairs import Solution


def test_ex1():
    nums = [1, 2, 3, 1, 1, 3]
    solution = Solution()
    result = solution.numIdenticalPairs(nums)
    assert result == 4


def test_ex2():
    nums = [1, 1, 1, 1]
    solution = Solution()
    result = solution.numIdenticalPairs(nums)
    assert result == 6


def test_ex3():
    nums = [1, 2, 3]
    solution = Solution()
    result = solution.numIdenticalPairs(nums)
    assert result == 0
