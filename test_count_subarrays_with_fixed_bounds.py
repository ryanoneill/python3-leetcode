from count_subarrays_with_fixed_bounds import Solution

def test_ex1():
    nums = [1,3,5,2,7,5]
    minK = 1
    maxK = 5
    solution = Solution()
    result = solution.countSubarrays(nums, minK, maxK)
    assert result == 2

def test_ex2():
    nums = [1,1,1,1]
    minK = 1
    maxK = 1
    solution = Solution()
    result = solution.countSubarrays(nums, minK, maxK)
    assert result == 10

def test_ex3():
    nums = [35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913] 
    minK = 35054
    maxK = 945315
    solution = Solution()
    result = solution.countSubarrays(nums, minK, maxK)
    assert result == 81

    # nums = [35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913] 
    # 0 35054 - min_count = 1
    # 1 398719
    # 2 945315 - max_count = 1 result = 1
    # 3 945315 - max_count = 2 result = 2
    # 4 820417                 result = 3
    # 5 945315 - max_count = 3 result = 4
    # 6 35054 - min_count = 2  result = 10
    # 7 945315                 result = 17
    # 8 171832                 result = 24
    # 9 945315                 result = 31
    # 10 35054                 result = 41
    # 11 109750                result = 51
    # 12 790964                result = 61
    # 13 441974                result = 71
    # 14 552913                result = 81
