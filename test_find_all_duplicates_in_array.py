from find_all_duplicates_in_array import Solution

# def test_ex1():
#     nums = [4,3,2,7,8,2,3,1]
#     solution = Solution()
#     result = solution.findDuplicates(nums)
#     assert result == [2,3]

def test_ex2():
    nums = [1,1,2]
    solution = Solution()
    result = solution.findDuplicates(nums)
    assert result == [1]

# def test_ex3():
#     nums = [1]
#     solution = Solution()
#     result = solution.findDuplicates(nums)
#     assert result == []
