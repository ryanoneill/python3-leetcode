from rotate_array import Solution

def test_ex1():
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution = Solution()
    solution.rotate(nums, k)
    assert nums == [5,6,7,1,2,3,4]

def test_ex2():
    nums = [-1, -100, 3, 99]
    k = 2
    solution = Solution()
    solution.rotate(nums, k)
    assert nums == [3,99,-1,-100]

def test_ex3():
    nums = [-1]
    k = 2
    solution = Solution()
    solution.rotate(nums, k)
    assert nums == [-1]
