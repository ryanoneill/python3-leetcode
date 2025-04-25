from count_good_triplets_in_array import Solution


def test_ex1():
    nums1 = [2, 0, 1, 3]
    nums2 = [0, 1, 2, 3]
    solution = Solution()
    result = solution.goodTriplets(nums1, nums2)
    assert result == 1


def test_ex2():
    nums1 = [4, 0, 1, 3, 2]
    nums2 = [4, 1, 0, 2, 3]
    solution = Solution()
    result = solution.goodTriplets(nums1, nums2)
    assert result == 4
