from sort_array_by_increasing_frequency import Solution

def test_ex1():
    nums = [1,1,2,2,2,3]
    solution = Solution()
    result = solution.frequencySort(nums)
    assert result == [3,1,1,2,2,2]

def test_ex2():
    nums = [2,3,1,3,2]
    solution = Solution()
    result = solution.frequencySort(nums)
    assert result == [1,3,3,2,2]

def test_ex3():
    nums = [-1,1,-6,4,5,-6,1,4,1]
    solution = Solution()
    result = solution.frequencySort(nums)
    assert result == [5,-1,4,4,-6,-6,1,1,1]
