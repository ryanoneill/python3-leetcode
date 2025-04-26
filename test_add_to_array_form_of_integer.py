from add_to_array_form_of_integer import Solution

def test_ex1():
    num = [1,2,0,0]
    k = 34
    solution = Solution()
    result = solution.addToArrayForm(num, k)
    assert result == [1,2,3,4]

def test_ex2():
    num = [2,7,4]
    k = 181
    solution = Solution()
    result = solution.addToArrayForm(num, k)
    assert result == [4,5,5]

def test_ex3():
    num = [2,1,5]
    k = 806
    solution = Solution()
    result = solution.addToArrayForm(num, k)
    assert result == [1,0,2,1]
