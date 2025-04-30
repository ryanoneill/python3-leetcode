from find_numbers_with_even_number_of_digits import Solution

def test_ex1():
    nums = [12,345,2,6,7896]
    solution = Solution()
    result = solution.findNumbers(nums)
    assert result == 2

def test_ex2():
    nums = [555,901,482,1771]
    solution = Solution()
    result = solution.findNumbers(nums)
    assert result == 1
