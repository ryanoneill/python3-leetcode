from typing import List
import math

class Solution:
    # Checks whether odd num is prime only
    def isPrime(self, num: int) -> bool:
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        result = [-1, -1]
        diff = right - left 

        start = left
        if start % 2 == 0:
            start += 1

        last_prime = -1
        if left == 1:
            start = 3
            last_prime = 2
        for i in range(start, right+1, 2):
            if self.isPrime(i):
                if last_prime == -1:
                    last_prime = i
                else:
                    current = i - last_prime
                    if current <= diff:
                        result = [last_prime, i]
                        diff = current
                        if diff <= 2:
                            break
                    last_prime = i
        return result


