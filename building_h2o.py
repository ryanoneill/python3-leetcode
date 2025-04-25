from typing import Callable
from threading import Barrier, Semaphore


class H2O:
    def __init__(self) -> None:
        self.barrier = Barrier(3)
        self.oxygen_sem = Semaphore(1)
        self.hydrogen_sem = Semaphore(2)

    def hydrogen(self, releaseHydrogen: "Callable[[], None]") -> None:
        with self.hydrogen_sem:
            self.barrier.wait()
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()

    def oxygen(self, releaseOxygen: "Callable[[], None]") -> None:
        with self.oxygen_sem:
            self.barrier.wait()
            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()
            self.barrier.reset()
