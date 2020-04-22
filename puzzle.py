class Puzzle:
    def __init__(self, board: list):
        self.board = board
        self.width = len(board)
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.priority = self.hamming()

    def __str__(self):
        out = ''
        for i in self.board:
            for j in i:
                out += str(j) + " "
            out += '\n'
        out += '\n'
        return out

    def hamming(self) -> int:
        hamming = 0
        for i in range(self.width):
            for j in range(self.width):
                if self.board[i][j] != self.goal[i][j] and self.board[i][j] != 0:
                    hamming += 1
        return hamming

    def find_zero(self) -> (int, int):
        for i in range(self.width):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    return i, j

    def move(self, puzzle: list, x1: int, y1: int, x2: int, y2: int) -> object or None:
        if 0 <= x2 < self.width and 0 <= y2 < self.width:
            temp_puz = self.copy(puzzle)
            temp_puz[x2][y2], temp_puz[x1][y1] = temp_puz[x1][y1], temp_puz[x2][y2]  # move!
            return temp_puz
        else:
            return None

    def copy(self, root):
        """ Copy function to create a similar matrix of the given board"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def create_nodes(self):
        x, y = self.find_zero()
        moves = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
        nodes = []
        for move in moves:
            child = self.move(self.board, x, y, move[0], move[1])  # self.board -> self
            if child is not None:
                node = Puzzle(child)
                nodes.append(node)
        return nodes

    def solve(self):
        root = self
        output = [root]
        prev_boards = [root.board]
        while root.board != self.goal:
            print(root)
            childs = root.create_nodes()
            for child in childs:
                if child.board in prev_boards:
                    childs.remove(child)
            childs.sort(key=lambda x: x.priority, reverse=False)
            root = childs[0]
            output.append(root)
            prev_boards.append(root.board)
        else:
            out = ''
            for j in output:
                out += str(j)
            return out



def main():
    test = [[0, 1, 3],
            [4, 2, 6],
            [7, 5, 8]]
    board = Puzzle(test)
    print(board.solve())


if __name__ == "__main__":
    main()
