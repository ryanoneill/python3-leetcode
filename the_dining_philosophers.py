from threading import Lock
from typing import Callable

class DiningPhilosophers:
    def __init__(self) -> None:
        self.locks = [Lock() for _ in range(5)]
        

    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork: Callable[[], None],
        pickRightFork: Callable[[], None],
        eat: Callable[[], None],
        putLeftFork: Callable[[], None],
        putRightFork: Callable[[], None],
    ) -> None:
        index = philosopher
        left = index
        right = (index + 1) % 5
        if index == 4:
            left, right = right, left

        with self.locks[left], self.locks[right]:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()

