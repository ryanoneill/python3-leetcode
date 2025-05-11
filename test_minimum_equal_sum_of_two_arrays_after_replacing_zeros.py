from minimum_equal_sum_of_two_arrays_after_replacing_zeros import Solution

def test_ex1():
    nums1 = [3,2,0,1,0]
    nums2 = [6,5,0]
    solution = Solution()
    result = solution.minSum(nums1, nums2)
    assert result == 12

def test_ex2():
    nums1 = [2,0,2,0]
    nums2 = [1,4]
    solution = Solution()
    result = solution.minSum(nums1, nums2)
    assert result == -1

def test_ex3():
    nums1 = [0,7,28,17,18]
    nums2 = [1,2,6,26,1,0,27,3,0,30]
    solution = Solution()
    result = solution.minSum(nums1, nums2)
    assert result == 98

def test_ex4():
    nums1 = [1,2,3,2]
    nums2 = [1,4,3]
    solution = Solution()
    result = solution.minSum(nums1, nums2)
    assert result == 8
