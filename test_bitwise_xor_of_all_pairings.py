from bitwise_xor_of_all_pairings import Solution

def test_ex1():
    nums1 = [2,1,3]
    nums2 = [10,2,5,0]
    solution = Solution()
    result = solution.xorAllNums(nums1, nums2)
    assert result == 13

def test_ex2():
    nums1 = [1,2]
    nums2 = [3,4]
    solution = Solution()
    result = solution.xorAllNums(nums1, nums2)
    assert result == 0
