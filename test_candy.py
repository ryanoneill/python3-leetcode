from candy import Solution

def test_ex1():
    ratings = [1,0,2]
    solution = Solution()
    result = solution.candy(ratings)
    assert result == 5

def test_ex2():
    ratings = [1,2,2]
    solution = Solution()
    result = solution.candy(ratings)
    assert result == 4
