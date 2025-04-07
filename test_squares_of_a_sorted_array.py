from squares_of_a_sorted_array import Solution


def test_ex1():
    nums = [-4, -1, 0, 3, 10]
    solution = Solution()
    result = solution.sortedSquares(nums)
    assert result == [0, 1, 9, 16, 100]


def test_ex2():
    nums = [-7, -3, 2, 3, 11]
    solution = Solution()
    result = solution.sortedSquares(nums)
    assert result == [4, 9, 9, 49, 121]


def test_ex3():
    nums = [-1]
    solution = Solution()
    result = solution.sortedSquares(nums)
    assert result == [1]
