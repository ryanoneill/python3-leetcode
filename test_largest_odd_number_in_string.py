from largest_odd_number_in_string import Solution

def test_ex1():
    num = "52"
    solution = Solution()
    result = solution.largestOddNumber(num)
    assert result == "5"

def test_ex2():
    num = "4206"
    solution = Solution()
    result = solution.largestOddNumber(num)
    assert result == ""

def test_ex3():
    num = "35427"
    solution = Solution()
    result = solution.largestOddNumber(num)
    assert result == "35427"
