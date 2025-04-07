from find_the_difference_of_two_arrays import Solution


def test_ex1():
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    solution = Solution()
    result = solution.findDifference(nums1, nums2)
    assert result == [[1, 3], [4, 6]]


def test_ex2():
    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    solution = Solution()
    result = solution.findDifference(nums1, nums2)
    assert result == [[3], []]
