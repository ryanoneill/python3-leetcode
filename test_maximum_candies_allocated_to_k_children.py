from maximum_candies_allocated_to_k_children import Solution

def test_ex1():
    candies = [5,6,8]
    k = 3
    solution = Solution()
    result = solution.maximumCandies(candies, k)
    assert result == 5

def test_ex2():
    candies = [2,5]
    k = 11
    solution = Solution()
    result = solution.maximumCandies(candies, k)
    assert result == 0

def test_ex3():
    candies = [10000000]
    k = 1000000000000
    solution = Solution()
    result = solution.maximumCandies(candies, k)
    assert result == 0

def test_ex4():
    candies = [4,7,5]
    k = 16
    solution = Solution()
    result = solution.maximumCandies(candies, k)
    assert result == 1
    
def test_ex5():
    candies = [9028315,1986242]
    k = 3030534
    solution = Solution()
    result = solution.maximumCandies(candies, k)
    assert result == 3
