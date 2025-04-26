from shuffle_the_array import Solution

def test_ex1():
    nums = [2,5,1,3,4,7]
    n = 3
    solution = Solution()
    result = solution.shuffle(nums, n)
    assert result == [2,3,5,4,1,7]

def test_ex2():
    nums = [1,2,3,4,4,3,2,1]
    n = 4
    solution = Solution()
    result = solution.shuffle(nums, n)
    assert result == [1,4,2,3,3,2,4,1]

def test_ex3():
    nums = [1,1,2,2]
    n = 2
    solution = Solution()
    result = solution.shuffle(nums, n)
    assert result == [1,2,1,2]


