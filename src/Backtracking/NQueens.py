class QueensProblem:

    def __init__(self, num_of_queens):
        """

        :param num_of_queens: size of the chess board a.k.a number of queens to be safely placed
        """
        self.num_of_queens = num_of_queens
        self.board = [[None for i in range(num_of_queens)] for j in range(num_of_queens)]

    def solve_queens_problem(self):

        if self.solve(0):
            self.print_board()
        else:
            print(" {0} queens cannot be safely placed together on a {0} by {0} chess board".format(self.num_of_queens))

    def solve(self, col):

        # Placement successful if we hit the base case
        if col == self.num_of_queens:
            return True

        # Iterate through the rows, trying to place the queen
        for row in range(self.num_of_queens):

            # check if the queen can be placed safely in the current row of the column
            if self.is_queen_safe(row, col):
                self.board[row][col] = 1

                # try to place the next queen in the next column
                if self.solve(col + 1):
                    return True
                else:
                    # backtrack if we were not able to place the next queen safely
                    self.board[row][col] = 0

        # if we don't hit the base case after iterating through all the rows and columns then solution is absent
        return False

    def is_queen_safe(self, row, col):
        """

        :param row: row in which we're trying to place the current queen
        :param col: col in which we're trying to place the current queen
        :return: True if the queen cannot be attacked by any other queen which is already placed on the board
        """

        """
        Note that the there shall be never a situation where we try and place two queens in the same column, therefore
        don't need to check for the presence of that situation in this method.
        
        Also, since we're trying to determine whether the current queen can be attacked by the preceding queens of not, 
        we should only look left of its current position.
        """

        # No two queens should be in the same row
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # No two queens should be placed diagonally to each other

        # towards north-west (left diagonal)
        j = col
        for i in range(row, -1, -1):

            if j < 0:
                break

            if self.board[i][j] == 1:
                return False

            j -= 1

        # towards south-west (right diagonal)
        j = col
        for i in range(row, len(self.board), 1):

            if j < 0:
                break

            if self.board[i][j] == 1:
                return False

            j -= 1

        return True

    def print_board(self):

        for row in range(self.num_of_queens):
            for col in range(self.num_of_queens):

                if self.board[row][col] == 1:
                    print(" Q ", end="")
                else:
                    print(" - ", end="")
            print('\n')


if __name__ == '__main__':
    qp = QueensProblem(8)
    qp.solve_queens_problem()
