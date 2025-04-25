from special_array_with_x_elements_greater_than_or_equal_x import Solution


def test_ex1():
    nums = [3, 5]
    solution = Solution()
    result = solution.specialArray(nums)
    assert result == 2


def test_ex2():
    nums = [0, 0]
    solution = Solution()
    result = solution.specialArray(nums)
    assert result == -1


def test_ex3():
    nums = [0, 4, 3, 0, 4]
    solution = Solution()
    result = solution.specialArray(nums)
    assert result == 3


def test_ex4():
    nums = [1000]
    solution = Solution()
    result = solution.specialArray(nums)
    assert result == 1
