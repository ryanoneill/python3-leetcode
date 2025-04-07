from typing import Callable
import threading


class Foo:
    def __init__(self):
        self.first_done = False
        self.first_condition = threading.Condition()

        self.second_done = False
        self.second_condition = threading.Condition()

    def first(self, printFirst: "Callable[[], None]") -> None:
        printFirst()
        with self.first_condition:
            self.first_done = True
            self.first_condition.notify()

    def second(self, printSecond: "Callable[[], None]") -> None:
        while not self.first_done:
            with self.first_condition:
                self.first_condition.wait()
        printSecond()
        with self.second_condition:
            self.second_done = True
            self.second_condition.notify()

    def third(self, printThird: "Callable[[], None]") -> None:
        while not self.second_done:
            with self.second_condition:
                self.second_condition.wait()
        printThird()
