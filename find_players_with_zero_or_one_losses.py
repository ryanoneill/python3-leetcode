from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = dict()
        for match in matches:
            winner = match[0]
            loser = match[1]
            if winner not in players:
                players[winner] = 0
            if loser not in players:
                players[loser] = 1
            else:
                players[loser] += 1
        zero_losses = []
        one_loss = []
        for key, value in players.items():
            if value == 0:
                zero_losses.append(key)
            elif value == 1:
                one_loss.append(key)
        zero_losses.sort()
        one_loss.sort()
        return [zero_losses, one_loss]
