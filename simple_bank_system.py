from typing import List


class Bank:
    def __init__(self, balance: List[int]) -> None:
        self.balances = balance
        self.accounts = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        result = False
        acc1_index = account1 - 1
        acc2_index = account2 - 1
        if 0 <= acc1_index < self.accounts and 0 <= acc2_index < self.accounts:
            if self.balances[acc1_index] >= money:
                self.balances[acc1_index] -= money
                self.balances[acc2_index] += money
                result = True
        return result

    def deposit(self, account: int, money: int) -> bool:
        result = False
        acc_index = account - 1
        if 0 <= acc_index < self.accounts:
            self.balances[acc_index] += money
            result = True
        return result

    def withdraw(self, account: int, money: int) -> bool:
        result = False
        acc_index = account - 1
        if 0 <= acc_index < self.accounts:
            if self.balances[acc_index] >= money:
                self.balances[acc_index] -= money
                result = True
        return result
