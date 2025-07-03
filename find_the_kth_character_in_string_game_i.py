class Solution:
    def __init__(self) -> None:
        self.value: str = "a"
        while len(self.value) < 500:
            self.value += "".join(self.next_character(letter) for letter in self.value)
        print(self.value)

    def next_character(self, letter: str) -> str:
        if letter == "z":
            result = "a"
        else:
            result = chr(ord(letter) + 1)
        return result

    def kthCharacter(self, k: int) -> str:
        addition = 0
        while k > 1:
            n = k.bit_length() - 1
            if (1 << n) == k:
                n -= 1
            k -= 1 << n
            addition += 1
        return chr(ord("a") + addition)
