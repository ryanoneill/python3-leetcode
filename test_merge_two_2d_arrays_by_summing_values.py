from merge_two_2d_arrays_by_summing_values import Solution

def test_ex1():
    nums1 = [[1,2],[2,3],[4,5]]
    nums2 = [[1,4],[3,2],[4,1]]
    solution = Solution()
    result = solution.mergeArrays(nums1, nums2)
    assert result == [[1,6],[2,3],[3,2],[4,6]]

def test_ex2():
    nums1 = [[2,4],[3,6],[5,5]]
    nums2 = [[1,3],[4,3]]
    solution = Solution()
    result = solution.mergeArrays(nums1, nums2)
    assert result == [[1,3],[2,4],[3,6],[4,3],[5,5]]
