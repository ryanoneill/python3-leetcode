from max_sum_of_a_pair_with_equal_sum_of_digits import Solution

def test_ex1():
    nums = [18,43,36,13,7]
    solution = Solution()
    result = solution.maximumSum(nums)
    assert result == 54

def test_ex2():
    nums = [10,12,19,14]
    solution = Solution()
    result = solution.maximumSum(nums)
    assert result == -1
