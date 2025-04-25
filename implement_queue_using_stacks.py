class MyQueue:
    def __init__(self) -> None:
        self.back = []
        self.front = []

    def push(self, x: int) -> None:
        self.back.append(x)

    def pop(self) -> int:
        if not self.front:
            self.front = list(reversed(self.back))
            self.back = []
        return self.front.pop()

    def peek(self) -> int:
        if not self.front:
            self.front = list(reversed(self.back))
            self.back = []
        return self.front[-1]

    def empty(self) -> bool:
        return not self.back and not self.front
