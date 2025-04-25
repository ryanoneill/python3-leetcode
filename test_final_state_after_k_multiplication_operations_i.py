from final_state_after_k_multiplication_operations_i import Solution


def test_ex1():
    nums = [2, 1, 3, 5, 6]
    k = 5
    multiplier = 2
    solution = Solution()
    result = solution.getFinalState(nums, k, multiplier)
    assert result == [8, 4, 6, 5, 6]


def test_ex2():
    nums = [1, 2]
    k = 3
    multiplier = 4
    solution = Solution()
    result = solution.getFinalState(nums, k, multiplier)
    assert result == [16, 8]
