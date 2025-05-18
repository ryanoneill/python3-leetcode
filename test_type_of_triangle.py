from type_of_triangle import Solution

def test_ex1():
    nums = [3,3,3]
    solution = Solution()
    result = solution.triangleType(nums)
    assert result == "equilateral"

def test_ex2():
    nums = [3,4,5]
    solution = Solution()
    result = solution.triangleType(nums)
    assert result == "scalene"

def test_ex3():
    nums = [1,1,2]
    solution = Solution()
    result = solution.triangleType(nums)
    assert result == "none"

def test_ex4():
    nums = [2,2,3]
    solution = Solution()
    result = solution.triangleType(nums)
    assert result == "isosceles"
