from minimum_operations_to_make_binary_array_elements_equal_to_one_i import Solution


def test_ex1():
    nums = [0, 1, 1, 1, 0, 0]
    solution = Solution()
    result = solution.minOperations(nums)
    assert result == 3


def test_ex2():
    nums = [0, 1, 1, 1]
    solution = Solution()
    result = solution.minOperations(nums)
    assert result == -1


def test_ex3():
    nums = [1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1]
    solution = Solution()
    result = solution.minOperations(nums)
    assert result == 9
