from count_the_number_of_good_subarrays import Solution

def test_ex1():
    nums = [1,1,1,1,1]
    k = 10
    solution = Solution()
    result = solution.countGood(nums, k)
    assert result == 1

def test_ex2():
    nums = [3,1,4,3,2,2,4]
    k = 2
    solution = Solution()
    result = solution.countGood(nums, k)
    assert result == 4
