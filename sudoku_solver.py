from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        regions = [set() for _ in range(9)]

        empties = []
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value != ".":
                    rows[i].add(value)
                    cols[j].add(value)
                    region_index = (i // 3) * 3 + (j // 3)
                    regions[region_index].add(value)
                else:
                    empties.append((i, j))

        n = len(empties)
        solved = [False]
        def worker(index: int):
            nonlocal solved
            if index == n:
                solved = [True]
            else:
                i, j = empties[index]
                
                for num in range(1,9+1):
                    region_index = (i // 3) * 3 + (j // 3)
                    attempt = str(num)
                    if attempt not in rows[i] and attempt not in cols[j] and attempt not in regions[region_index]:
                        rows[i].add(attempt)
                        cols[j].add(attempt)
                        regions[region_index].add(attempt)
                        board[i][j] = attempt
                        worker(index+1)
                        if not solved[0]:
                            board[i][j] = "."
                            rows[i].remove(attempt)
                            cols[j].remove(attempt)
                            regions[region_index].remove(attempt)

        worker(0)
