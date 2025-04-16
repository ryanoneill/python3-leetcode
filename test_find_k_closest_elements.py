from find_k_closest_elements import Solution

def test_ex1():
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    solution = Solution()
    result = solution.findClosestElements(arr, k, x)
    assert result == [1,2,3,4]

def test_ex2():
    arr = [1,1,2,3,4,5]
    k = 4
    x = -1
    solution = Solution()
    result = solution.findClosestElements(arr, k, x)
    assert result == [1,1,2,3]

