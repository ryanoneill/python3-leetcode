from typing import Callable
from threading import Condition

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizz_ready = False
        self.fizz_condition = Condition()

        self.buzz_ready = False
        self.buzz_condition = Condition()

        self.fizzbuzz_ready = False
        self.fizzbuzz_condition = Condition()

        self.number_ready = True
        self.number_condition = Condition()

        self.done = False

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while not self.done:
            with self.fizz_condition:
                self.fizz_condition.wait_for(lambda: self.fizz_ready)
                if not self.done:
                    printFizz()
                    self.fizz_ready = False
                    with self.number_condition:
                        self.number_ready = True
                        self.number_condition.notify()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while not self.done:
            with self.buzz_condition:
                self.buzz_condition.wait_for(lambda: self.buzz_ready)
                if not self.done:
                    printBuzz()
                    self.buzz_ready = False
                    with self.number_condition:
                        self.number_ready = True
                        self.number_condition.notify()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while not self.done:
            with self.fizzbuzz_condition:
                self.fizzbuzz_condition.wait_for(lambda: self.fizzbuzz_ready)
                if not self.done:
                    printFizzBuzz()
                    self.fizzbuzz_ready = False
                    with self.number_condition:
                        self.number_ready = True
                        self.number_condition.notify()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            with self.number_condition:
                self.number_condition.wait_for(lambda: self.number_ready)
                if i % 3 == 0 and i % 5 == 0:
                    self.number_ready = False
                    with self.fizzbuzz_condition:
                        self.fizzbuzz_ready = True
                        self.fizzbuzz_condition.notify()
                elif i % 3 == 0:
                    self.number_ready = False
                    with self.fizz_condition:
                        self.fizz_ready = True
                        self.fizz_condition.notify()
                elif i % 5 == 0:
                    self.number_ready = False
                    with self.buzz_condition:
                        self.buzz_ready = True
                        self.buzz_condition.notify()
                else:
                    printNumber(i)

        with self.number_condition:
            # Cleanup
            self.number_condition.wait_for(lambda: self.number_ready)
            self.done = True
            with self.fizz_condition:
                self.fizz_ready = True
                self.fizz_condition.notify()
            with self.buzz_condition:
                self.buzz_ready = True
                self.buzz_condition.notify()
            with self.fizzbuzz_condition:
                self.fizzbuzz_ready = True
                self.fizzbuzz_condition.notify()

