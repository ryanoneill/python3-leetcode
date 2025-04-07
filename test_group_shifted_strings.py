from group_shifted_strings import Solution


def test_ex1():
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    solution = Solution()
    results = solution.groupStrings(strings)
    expected = [["acef"], ["a", "z"], ["abc", "bcd", "xyz"], ["az", "ba"]]
    assert sorted(results) == sorted(expected)


def test_ex2():
    strings = ["a"]
    solution = Solution()
    results = solution.groupStrings(strings)
    assert results == [["a"]]
