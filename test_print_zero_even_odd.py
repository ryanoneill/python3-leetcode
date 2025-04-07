from print_zero_even_odd import ZeroEvenOdd
from threading import Thread


class ZeroEvenOddTester:
    def __init__(self, zeo):
        self.data = ""
        self.zeo = zeo
        self.zero_thread = Thread(target=zeo.zero, args=[self.printNumber])
        self.odd_thread = Thread(target=zeo.odd, args=[self.printNumber])
        self.even_thread = Thread(target=zeo.even, args=[self.printNumber])

    def printNumber(self, value: int):
        self.data += str(value)

    def run(self):
        self.zero_thread.start()
        self.odd_thread.start()
        self.even_thread.start()

        self.zero_thread.join()
        self.odd_thread.join()
        self.even_thread.join()

        return self.data


def test_ex1():
    n = 2
    zeo = ZeroEvenOdd(n)
    zeot = ZeroEvenOddTester(zeo)
    result = zeot.run()
    assert result == "0102"


def test_ex2():
    n = 5
    zeo = ZeroEvenOdd(n)
    zeot = ZeroEvenOddTester(zeo)
    result = zeot.run()
    assert result == "0102030405"
