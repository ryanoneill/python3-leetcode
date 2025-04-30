from heapq import heapify, heappop, heappush

class SeatManager:
    def __init__(self, n: int) -> None:
        self.n = n
        self.available = list(range(1, n+1))
        heapify(self.available)

    def reserve(self) -> int:
        result = heappop(self.available)
        return result

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.available, seatNumber)
