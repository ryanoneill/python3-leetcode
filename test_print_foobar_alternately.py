from print_foobar_alternately import FooBar
from threading import Thread


class FooBarTester:
    def __init__(self, foobar):
        self.data = ""
        self.foobar = foobar
        self.t_foo = Thread(target=foobar.foo, args=[self.printFoo])
        self.t_bar = Thread(target=foobar.bar, args=[self.printBar])

    def printFoo(self):
        self.data += "foo"

    def printBar(self):
        self.data += "bar"

    def run(self) -> str:
        self.t_bar.start()
        self.t_foo.start()

        self.t_bar.join()
        self.t_foo.join()

        return self.data


def test_ex1():
    n = 1
    foobar = FooBar(n)
    fbt = FooBarTester(foobar)
    result = fbt.run()
    assert result == "foobar"


def test_ex2():
    n = 2
    foobar = FooBar(n)
    fbt = FooBarTester(foobar)
    result = fbt.run()
    assert result == "foobarfoobar"
