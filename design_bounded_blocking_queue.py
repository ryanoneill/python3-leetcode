from collections import deque
from threading import Semaphore

# TODO: Implement Test for This
class BoundedBlockingQueue(object):
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.values = deque()
        self.enq_sem = Semaphore(capacity)
        self.deq_sem = Semaphore(0)

    def enqueue(self, element: int) -> None:
        self.enq_sem.acquire()
        self.values.append(element)
        self.deq_sem.release()

    def dequeue(self) -> int:
        self.deq_sem.acquire()
        result = self.values.popleft()
        self.enq_sem.release()
        return result

    def size(self) -> int:
        return len(self.values)

