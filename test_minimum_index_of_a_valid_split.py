from minimum_index_of_a_valid_split import Solution

def test_ex1():
    nums = [1,2,2,2]
    solution = Solution()
    result = solution.minimumIndex(nums)
    assert result == 2

def test_ex2():
    nums = [2,1,3,1,1,1,7,1,2,1]  
    solution = Solution()
    result = solution.minimumIndex(nums)
    assert result == 4

def test_ex3():
    nums = [3,3,3,3,7,2,2]
    solution = Solution()
    result = solution.minimumIndex(nums)
    assert result == -1
