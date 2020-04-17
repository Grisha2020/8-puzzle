import numpy as np
import beautifultable as bt


class Node:
    def __init__(self, data, level, fval):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data
        self.level = level
        self.finalvalue = fval


class Puzzle:
    def __init__(self, board: list):
        self.board = board
        self.width = len(board)
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def accept(self):
        pass

    def __repr__(self):
        table = bt.BeautifulTable()
        for k in range(self.width):
            table.append_row(self.board[k])
        return str(table)

    def get_idx(self, board, value) -> (int, int):
        for i in range(self.width):
            for j in range(self.width):
                if board[i][j] == value:
                    return i, j

    def solved(self) -> bool:
        return self.board == self.goal

    def hamming(self) -> int:
        hamming = 0
        for i in range(self.width):
            for j in range(self.width):
                if self.board[i][j] != self.goal[i][j] and self.board[i][j] != 0:
                    hamming += 1
        return hamming

    def manhattan(self) -> int:
        manhattan = 0
        for i in range(self.width):
            for j in range(self.width):
                my_num = self.board[i][j]
                x, y = self.get_idx(self.goal, my_num)
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
