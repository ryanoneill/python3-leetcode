class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0

        for i, letter in enumerate(colors):
            if i >= 2:
                if letter == colors[i-1] and letter == colors[i-2]:
                    if letter == "A":
                        alice += 1
                    else:
                        bob += 1


        return alice > bob
