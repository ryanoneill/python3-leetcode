from threading import Lock

# TODO: Create Multithreaded Driver Test Harness
class TrafficLight:
    def __init__(self):
        self.lock = Lock()
        self.green_road = 1

    def carArrived(
        self,
        carId: int,
        roadId: int,
        direction: int,
        turnGreen: 'Callable[[], None]',
        crossCar: 'Callable[[], None]'
    ) -> None:
        with self.lock:
            if self.green_road != roadId:
                turnGreen()
                self.green_road = roadId
            crossCar()
