from find_the_kth_largest_integer_in_the_array import Solution

def test_ex1():
    nums = ["3","6","7","10"]
    k = 4
    solution = Solution()
    result = solution.kthLargestNumber(nums, k)
    assert result == "3"

def test_ex2():
    nums = ["2", "21", "12", "1"]
    k = 3
    solution = Solution()
    result = solution.kthLargestNumber(nums, k)
    assert result == "2"

def test_ex3():
    nums = ["0", "0"]
    k = 2
    solution = Solution()
    result = solution.kthLargestNumber(nums, k)
    assert result == "0"
