class StockSpanner:
    def __init__(self):
        self.values = []
        self.day = 0

    def next(self, price: int) -> int:
        self.day += 1
        while self.values:
            (p_day, p_price) = self.values[-1]
            if price >= p_price:
                self.values.pop()
            else:
                break
        result = self.day
        if self.values:
            (p_day, _) = self.values[-1]
            result = self.day - p_day
        self.values.append((self.day, price))
        return result
