from length_of_longest_fibonacci_subsequence import Solution

def test_ex1():
    arr = [1,2,3,4,5,6,7,8]
    solution = Solution()
    result = solution.lenLongestFibSubseq(arr)
    assert result == 5

def test_ex2():
    arr = [1,3,7,11,12,14,18]
    solution = Solution()
    result = solution.lenLongestFibSubseq(arr)
    assert result == 3
