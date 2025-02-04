from wiggle_sort import Solution

def test_ex1():
    nums = [3,5,2,1,6,4]
    solution = Solution()
    solution.wiggleSort(nums)
    assert nums == [3,5,1,6,2,4]

def test_ex2():
    nums = [6,6,5,6,3,8]
    solution = Solution()
    solution.wiggleSort(nums)
    assert nums == [6,6,5,6,3,8]
