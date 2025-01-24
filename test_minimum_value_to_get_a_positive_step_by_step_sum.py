from minimum_value_to_get_a_positive_step_by_step_sum import Solution

def test_ex1():
    nums = [-3,2,-3,4,2]
    solution = Solution()
    result = solution.minStartValue(nums)
    assert result == 5

def test_ex2():
    nums = [1,2]
    solution = Solution()
    result = solution.minStartValue(nums)
    assert result == 1

def test_ex3():
    nums = [1,-2,-3]
    solution = Solution()
    result = solution.minStartValue(nums)
    assert result == 5
