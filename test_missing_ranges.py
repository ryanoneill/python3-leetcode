from missing_ranges import Solution


def test_ex1():
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    solution = Solution()
    results = solution.findMissingRanges(nums, lower, upper)
    assert results == [[2, 2], [4, 49], [51, 74], [76, 99]]


def test_ex2():
    nums = [-1]
    lower = -1
    upper = -1
    solution = Solution()
    results = solution.findMissingRanges(nums, lower, upper)
    assert results == []


def test_ex3():
    nums = [-1]
    lower = -2
    upper = -1
    solution = Solution()
    results = solution.findMissingRanges(nums, lower, upper)
    assert results == [[-2, -2]]


def test_ex4():
    nums = []
    lower = 1
    upper = 1
    solution = Solution()
    results = solution.findMissingRanges(nums, lower, upper)
    assert results == [[1, 1]]
