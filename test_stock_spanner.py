from stock_spanner import StockSpanner

def test_ex1():
    stock_spanner = StockSpanner()
    result = stock_spanner.next(100)
    assert result == 1
    result = stock_spanner.next(80)
    assert result == 1
    result = stock_spanner.next(60)
    assert result == 1
    result = stock_spanner.next(70)
    assert result == 2
    result = stock_spanner.next(60)
    assert result == 1
    result = stock_spanner.next(75)
    assert result == 4
    result = stock_spanner.next(85)
    assert result == 6

def test_ex2():
    stock_spanner = StockSpanner()
    result = stock_spanner.next(28)
    assert result == 1
    result = stock_spanner.next(14)
    assert result == 1
    result = stock_spanner.next(28)
    assert result == 3
    result = stock_spanner.next(35)
    assert result == 4
    result = stock_spanner.next(46)
    assert result == 5
    result = stock_spanner.next(53)
    assert result == 6
    result = stock_spanner.next(66)
    assert result == 7
    result = stock_spanner.next(80)
    assert result == 8
    result = stock_spanner.next(87)
    assert result == 9
    result = stock_spanner.next(88)
    assert result == 10
