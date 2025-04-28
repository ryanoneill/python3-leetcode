from sort_integers_by_the_number_of_1_bits import Solution

def test_ex1():
    arr = [0,1,2,3,4,5,6,7,8]
    solution = Solution()
    result = solution.sortByBits(arr)
    assert result == [0,1,2,4,8,3,5,6,7]

def test_ex2():
    arr = [1024,512,256,128,64,32,16,8,4,2,1]
    solution = Solution()
    result = solution.sortByBits(arr)
    assert result == [1,2,4,8,16,32,64,128,256,512,1024]
