from sort_characters_by_frequency import Solution

def test_ex1():
    s = "tree"
    solution = Solution()
    result = solution.frequencySort(s)
    assert result == "eert"

def test_ex2():
    s = "cccaaa"
    solution = Solution()
    result = solution.frequencySort(s)
    assert result == "aaaccc"

def test_ex3():
    s = "Aaab"
    solution = Solution()
    result = solution.frequencySort(s)
    assert result == "aaAb"
