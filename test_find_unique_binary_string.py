from find_unique_binary_string import Solution


def test_ex1():
    nums = ["01", "10"]
    solution = Solution()
    result = solution.findDifferentBinaryString(nums)
    assert result == "00"


def test_ex2():
    nums = ["00", "01"]
    solution = Solution()
    result = solution.findDifferentBinaryString(nums)
    assert result == "10"


def test_ex3():
    nums = ["111", "011", "001"]
    solution = Solution()
    result = solution.findDifferentBinaryString(nums)
    assert result == "000"
