from sort_the_people import Solution

def test_ex1():
    names = ["Mary","John","Emma"]
    heights = [180,165,170]
    solution = Solution()
    results = solution.sortPeople(names, heights)
    assert results == ["Mary","Emma","John"]

def test_ex2():
    names = ["Alice","Bob","Bob"]
    heights = [155,185,150]
    solution = Solution()
    results = solution.sortPeople(names, heights)
    assert results == ["Bob","Alice","Bob"]
