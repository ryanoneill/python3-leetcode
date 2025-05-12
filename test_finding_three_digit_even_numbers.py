from finding_three_digit_even_numbers import Solution

def test_ex1():
    digits = [2,1,3,0]
    solution = Solution()
    result = solution.findEvenNumbers(digits)
    assert result == [102,120,130,132,210,230,302,310,312,320]

def test_ex2():
    digits = [2,2,8,8,2]
    solution = Solution()
    result = solution.findEvenNumbers(digits)
    assert result == [222,228,282,288,822,828,882]

def test_ex3():
    digits = [3,7,5]
    solution = Solution()
    result = solution.findEvenNumbers(digits)
    assert result == []

def test_ex4():
    digits = [1,0,0,1]
    solution = Solution()
    result = solution.findEvenNumbers(digits)
    assert result == [100,110]

def test_ex5():
    digits = [9,9,9,8,1,0]
    solution = Solution()
    result = solution.findEvenNumbers(digits)
    assert result == [108,180,190,198,810,890,908,910,918,980,990,998]
