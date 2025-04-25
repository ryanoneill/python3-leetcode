from destination_city import Solution


def test_ex1():
    paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    solution = Solution()
    result = solution.destCity(paths)
    assert result == "Sao Paulo"


def test_ex2():
    paths = [["B", "C"], ["D", "B"], ["C", "A"]]
    solution = Solution()
    result = solution.destCity(paths)
    assert result == "A"


def test_ex3():
    paths = [["A", "Z"]]
    solution = Solution()
    result = solution.destCity(paths)
    assert result == "Z"
