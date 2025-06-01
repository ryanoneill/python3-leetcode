from distribute_candies import Solution

def test_ex1():
    candyType = [1,1,2,2,3,3]
    solution = Solution()
    result = solution.distributeCandies(candyType)
    assert result == 3

def test_ex2():
    candyType = [1,1,2,3]
    solution = Solution()
    result = solution.distributeCandies(candyType)
    assert result == 2

def test_ex3():
    candyType = [6,6,6,6]
    solution = Solution()
    result = solution.distributeCandies(candyType)
    assert result == 1
