from first_unique_number import FirstUnique

def test_ex1():
    nums = [2,3,5]
    fu = FirstUnique(nums)
    result = fu.showFirstUnique()
    assert result == 2
    fu.add(5)
    result = fu.showFirstUnique()
    assert result == 2
    fu.add(2)
    result = fu.showFirstUnique()
    assert result == 3
    fu.add(3)
    result = fu.showFirstUnique()
    assert result == -1

def test_ex2():
    nums = [7,7,7,7,7,7]
    fu = FirstUnique(nums)
    result = fu.showFirstUnique()
    assert result == -1
    fu.add(7)
    fu.add(3)
    fu.add(3)
    fu.add(7)
    fu.add(17)
    result = fu.showFirstUnique()
    assert result == 17

def test_ex3():
    nums = [809]
    fu = FirstUnique(nums)
    result = fu.showFirstUnique()
    assert result == 809
    fu.add(809)
    result = fu.showFirstUnique()
    assert result == -1
