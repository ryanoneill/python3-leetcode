from largest_three_same_digit_number_in_string import Solution

def test_ex1():
    num = "6777133339"
    solution = Solution()
    result = solution.largestGoodInteger(num)
    assert result == "777"

def test_ex2():
    num = "2300019"
    solution = Solution()
    result = solution.largestGoodInteger(num)
    assert result == "000"

def test_ex3():
    num = "42352338"
    solution = Solution()
    result = solution.largestGoodInteger(num)
    assert result == ""
