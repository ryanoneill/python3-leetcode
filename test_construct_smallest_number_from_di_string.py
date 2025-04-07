from construct_smallest_number_from_di_string import Solution


def test_ex1():
    pattern = "IIIDIDDD"
    solution = Solution()
    result = solution.smallestNumber(pattern)
    assert result == "123549876"


def test_ex2():
    pattern = "DDD"
    solution = Solution()
    result = solution.smallestNumber(pattern)
    assert result == "4321"
