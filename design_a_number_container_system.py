class NumberContainers:
    def __init__(self):
        self.by_container = {}
        self.by_number = {}

        self.min_by_number = {}

    def change(self, index: int, number: int) -> None:
        if index in self.by_container:
            previous = self.by_container[index]
            self.by_number[previous].remove(index)
            if len(self.by_number[previous]) == 0:
                del self.by_number[previous]
                del self.min_by_number[previous]
            elif self.min_by_number[previous] == index:
                self.min_by_number[previous] = min(self.by_number[previous])
        self.by_container[index] = number
        if number in self.by_number:
            self.by_number[number].add(index)
        else:
            self.by_number[number] = {index}
        if number in self.min_by_number:
            self.min_by_number[number] = min(index, self.min_by_number[number])
        else:
            self.min_by_number[number] = index

    def find(self, number: int) -> int:
        result = -1
        if number in self.min_by_number:
            result = self.min_by_number[number]
        return result
