from longest_strictly_increasing_or_strictly_decreasing_subarray import Solution


def test_ex1():
    nums = [1, 4, 3, 3, 2]
    solution = Solution()
    result = solution.longestMonotonicSubarray(nums)
    assert result == 2


def test_ex2():
    nums = [3, 3, 3, 3]
    solution = Solution()
    result = solution.longestMonotonicSubarray(nums)
    assert result == 1


def test_ex3():
    nums = [3, 2, 1]
    solution = Solution()
    result = solution.longestMonotonicSubarray(nums)
    assert result == 3
