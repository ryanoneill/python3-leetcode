from typing import List
from print_in_order import Foo
from threading import Thread


class PrintTester:
    def __init__(self, foo):
        self.data = ""
        self.foo = foo
        self.t1 = Thread(target=foo.first, args=[self.printFirst])
        self.t2 = Thread(target=foo.second, args=[self.printSecond])
        self.t3 = Thread(target=foo.third, args=[self.printThird])

    def printFirst(self):
        self.data += "first"

    def printSecond(self):
        self.data += "second"

    def printThird(self):
        self.data += "third"

    def getResults(self) -> str:
        return self.data

    def run(self, nums: List[int]) -> str:
        for num in nums:
            if num == 1:
                self.t1.start()
            elif num == 2:
                self.t2.start()
            elif num == 3:
                self.t3.start()
            else:
                raise f"unknown num {num}"

        self.t1.join()
        self.t2.join()
        self.t3.join()

        return self.getResults()


def test_ex1():
    nums = [1, 2, 3]
    foo = Foo()
    pt = PrintTester(foo)
    result = pt.run(nums)
    assert result == "firstsecondthird"


def test_ex2():
    nums = [1, 3, 2]
    foo = Foo()
    pt = PrintTester(foo)
    result = pt.run(nums)
    assert result == "firstsecondthird"


def test_ex3():
    nums = [3, 2, 1]
    foo = Foo()
    pt = PrintTester(foo)
    result = pt.run(nums)
    assert result == "firstsecondthird"
