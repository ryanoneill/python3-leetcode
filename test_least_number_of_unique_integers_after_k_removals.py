from least_number_of_unique_integers_after_k_removals import Solution

def test_ex1():
    arr = [5,5,4]
    k = 1
    solution = Solution()
    result = solution.findLeastNumOfUniqueInts(arr, k)
    assert result == 1

def test_ex2():
    arr = [4,3,1,1,3,3,2]
    k = 3
    solution = Solution()
    result = solution.findLeastNumOfUniqueInts(arr, k)
    assert result == 2

