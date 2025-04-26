from lucky_numbers_in_a_matrix import Solution

def test_ex1():
    matrix = [[3,7,8],[9,11,13],[15,16,17]]
    solution = Solution()
    result = solution.luckyNumbers(matrix)
    assert result == [15]

def test_ex2():
    matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]  
    solution = Solution()
    result = solution.luckyNumbers(matrix)
    assert result == [12]

def test_ex3():
    matrix = [[7,8],[1,2]]
    solution = Solution()
    result = solution.luckyNumbers(matrix)
    assert result == [7]
