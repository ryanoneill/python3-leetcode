from threading import Condition
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.foo_ready = True
        self.foo_condition = Condition()
        self.n = n

    def foo(self, printFoo: "Callable[[], None]") -> None:
        for i in range(self.n):
            with self.foo_condition:
                self.foo_condition.wait_for(lambda: self.foo_ready)
                printFoo()
                self.foo_ready = False
                self.foo_condition.notify()

    def bar(self, printBar: "Callable[[], None]") -> None:
        for i in range(self.n):
            with self.foo_condition:
                self.foo_condition.wait_for(lambda: not self.foo_ready)
                printBar()
                self.foo_ready = True
                self.foo_condition.notify()
