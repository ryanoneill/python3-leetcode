from binary_search import Solution


def test_ex1():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    solution = Solution()
    result = solution.search(nums, target)
    assert result == 4


def test_ex2():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    solution = Solution()
    result = solution.search(nums, target)
    assert result == -1
