from next_greater_element_i import Solution

def test_ex1():
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    solution = Solution()
    result = solution.nextGreaterElement(nums1, nums2)
    assert result == [-1,3,-1]

def test_ex2():
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    solution = Solution()
    result = solution.nextGreaterElement(nums1, nums2)
    assert result == [3,-1]
