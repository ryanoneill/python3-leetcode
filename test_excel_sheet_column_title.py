from excel_sheet_column_title import Solution


def test_ex1():
    columnNumber = 1
    solution = Solution()
    result = solution.convertToTitle(columnNumber)
    assert result == "A"


def test_ex2():
    columnNumber = 28
    solution = Solution()
    result = solution.convertToTitle(columnNumber)
    assert result == "AB"


def test_ex3():
    columnNumber = 701
    solution = Solution()
    result = solution.convertToTitle(columnNumber)
    assert result == "ZY"
