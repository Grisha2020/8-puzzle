import numpy as np
import beautifultable as bt


class Puzzle:

    def __init__(self, board: list):
        self.board = board
        self.width = len(board)
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.goal_idx = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), 0: (2, 2)
        }

    def __repr__(self):
        table = bt.BeautifulTable()
        for k in range(self.width):
            table.append_row(self.board[k])
        return str(table)

    def solved(self) -> bool:
        return self.board == self.goal

    def hamming(self) -> int:
        hamming = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != self.goal[i][j] and self.board[i][j] != 0:
                    hamming += 1
        return hamming

    def manhattan(self) -> int:
        manhattan = 0
        for i in range(3):
            for j in range(3):
                my_num = self.board[i][j]
                x, y = self.goal_idx[my_num]
                manhattan += abs((x + y) - (i + j))
        return manhattan




def main():
    quiz = [[8, 1, 3], [4, 0, 2], [7, 6, 5]]
    board = Puzzle(quiz)
    print(board)
    print(board.hamming())
    print(board.manhattan())


if __name__ == "__main__":
    main()
