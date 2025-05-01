from maximum_length_of_repeated_subarray import Solution

def test_ex1():
    nums1 = [1,2,3,2,1]
    nums2 = [3,2,1,4,7]
    solution = Solution()
    result = solution.findLength(nums1, nums2)
    assert result == 3

def test_ex2():
    nums1 = [0,0,0,0,0]
    nums2 = [0,0,0,0,0]
    solution = Solution()
    result = solution.findLength(nums1, nums2)
    assert result == 5

def test_ex3():
    nums1 = [1,1,0,0,1,1]
    nums2 = [0,0]
    solution = Solution()
    result = solution.findLength(nums1, nums2)
    assert result == 2
