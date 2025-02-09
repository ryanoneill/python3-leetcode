from fizz_buzz_multithreaded import FizzBuzz
from threading import Thread
from typing import List

class FizzBuzzTester:
    def __init__(self, fizzbuzz):
        self.data = []
        self.fizzbuzz = fizzbuzz
        self.t_fizz = Thread(name="fizz", target=fizzbuzz.fizz, args=[self.printFizz])
        self.t_buzz = Thread(name="buzz", target=fizzbuzz.buzz, args=[self.printBuzz])
        self.t_fizzbuzz = Thread(name="fizzbuzz", target=fizzbuzz.fizzbuzz, args=[self.printFizzBuzz])
        self.t_number = Thread(name="number", target=fizzbuzz.number, args=[self.printNumber])

    def printFizz(self):
        print("fizz")
        self.data.append("fizz")

    def printBuzz(self):
        print("buzz")
        self.data.append("buzz")

    def printFizzBuzz(self):
        print("fizzbuzz")
        self.data.append("fizzbuzz")

    def printNumber(self, i: int):
        print(str(i))
        self.data.append(str(i))

    def run(self) -> List[str]:
        self.t_fizz.start()
        self.t_buzz.start()
        self.t_fizzbuzz.start()
        self.t_number.start()

        self.t_fizz.join()
        self.t_buzz.join()
        self.t_fizzbuzz.join()
        self.t_number.join()

        return self.data


def test_ex1():
    n = 15
    fizzbuzz = FizzBuzz(n)
    fbt = FizzBuzzTester(fizzbuzz)
    result = fbt.run()
    assert result == ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizzbuzz"]

def test_ex2():
    n = 8
    fizzbuzz = FizzBuzz(n)
    fbt = FizzBuzzTester(fizzbuzz)
    result = fbt.run()
    assert result == ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8"]
