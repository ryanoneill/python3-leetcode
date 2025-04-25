from typing import Callable
from threading import Event


class Foo:
    def __init__(self):
        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst: "Callable[[], None]") -> None:
        printFirst()
        self.first_done.set()

    def second(self, printSecond: "Callable[[], None]") -> None:
        while not self.first_done.is_set():
            self.first_done.wait()
        printSecond()
        self.second_done.set()

    def third(self, printThird: "Callable[[], None]") -> None:
        while not self.second_done.is_set():
            self.second_done.wait()
        printThird()
