from simple_bank_system import Bank


def test_ex1():
    bank = Bank([10, 100, 20, 50, 30])
    assert bank.withdraw(3, 10)
    assert bank.transfer(5, 1, 20)
    assert bank.deposit(5, 20)
    assert not bank.transfer(3, 4, 15)
    assert not bank.withdraw(10, 50)
