from count_subarrays_where_max_element_appears_at_least_k_times import Solution

def test_ex1():
    nums = [1,3,2,3,3]
    k = 2
    solution = Solution()
    result = solution.countSubarrays(nums, k)
    assert result == 6

def test_ex2():
    nums = [1,4,2,1]
    k = 3
    solution = Solution()
    result = solution.countSubarrays(nums, k)
    assert result == 0

def test_ex3():
    nums = [61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82]
    k = 2
    solution = Solution()
    result = solution.countSubarrays(nums, k)
    assert result == 224

def test_ex4():
    nums = [2,2,2,2,1,3,3,2,2,1,1,3,1,1,2,3,2,1,1,2,1,1,2,1,2,1,2,1,3,1,3,3]
    k = 5
    solution = Solution()
    result = solution.countSubarrays(nums, k)
    assert result == 31

