from intersection_of_two_arrays import Solution

def test_ex1():
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    solution = Solution()
    result = solution.intersection(nums1, nums2)
    assert result == [2]

def test_ex2():
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    solution = Solution()
    results = solution.intersection(nums1, nums2)
    results.sort()
    assert results == [4,9]
