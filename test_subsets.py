from subsets import Solution


def test_ex1():
    nums = [1, 2, 3]
    solution = Solution()
    results = solution.subsets(nums)
    results.sort()
    assert results == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
