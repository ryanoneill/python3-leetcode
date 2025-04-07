from enum import Enum
from typing import Callable
from threading import Condition


class State(Enum):
    ZERO = 1
    ODD = 2
    EVEN = 3


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.state = State.ZERO
        self.state_condition = Condition()

    def zero(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(1, self.n + 1):
            with self.state_condition:
                self.state_condition.wait_for(lambda: self.state == State.ZERO)
                printNumber(0)
                if i % 2 == 1:
                    self.state = State.ODD
                else:
                    self.state = State.EVEN
                self.state_condition.notify_all()

    def even(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                with self.state_condition:
                    self.state_condition.wait_for(lambda: self.state == State.EVEN)
                    printNumber(i)
                    self.state = State.ZERO
                    self.state_condition.notify_all()

    def odd(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(1, self.n + 1):
            if i % 2 == 1:
                with self.state_condition:
                    self.state_condition.wait_for(lambda: self.state == State.ODD)
                    printNumber(i)
                    self.state = State.ZERO
                    self.state_condition.notify_all()
