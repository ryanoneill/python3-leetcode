from number_of_subsequences_that_satisfy_the_given_sum_condition import Solution

def test_ex1():
    nums = [3,5,6,7]
    target = 9
    solution = Solution()
    result = solution.numSubseq(nums, target)
    assert result == 4

def test_ex2():
    nums = [3,3,6,8]
    target = 10
    solution = Solution()
    result = solution.numSubseq(nums, target)
    assert result == 6

def test_ex3():
    nums = [2,3,3,4,6,7]
    target = 12
    solution = Solution()
    result = solution.numSubseq(nums, target)
    assert result == 61
