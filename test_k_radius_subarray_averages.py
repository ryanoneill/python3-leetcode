from k_radius_subarray_averages import Solution

def test_ex1():
    nums = [7,4,3,9,1,8,5,2,6]
    k = 3
    solution = Solution()
    result = solution.getAverages(nums, k)
    assert result == [-1,-1,-1,5,4,4,-1,-1,-1]

def test_ex2():
    nums = [100000]
    k = 0
    solution = Solution()
    result = solution.getAverages(nums, k)
    assert result == [100000]

def test_ex3():
    nums = [8]
    k = 100000
    solution = Solution()
    result = solution.getAverages(nums, k)
    assert result == [-1]
