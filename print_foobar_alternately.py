from threading import Event
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.foo_ready = Event()
        self.bar_ready = Event()
        self.n = n
        self.foo_ready.set()


    def foo(self, printFoo: "Callable[[], None]") -> None:
        for _ in range(self.n):
            while not self.foo_ready.is_set():
                self.foo_ready.wait()
            printFoo()
            self.foo_ready.clear()
            self.bar_ready.set()


    def bar(self, printBar: "Callable[[], None]") -> None:
        for _ in range(self.n):
            while not self.bar_ready.is_set():
                self.bar_ready.wait()
            printBar()
            self.bar_ready.clear()
            self.foo_ready.set()
