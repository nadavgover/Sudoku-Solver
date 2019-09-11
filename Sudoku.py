import time


class Sudoku:
    def __init__(self, lines):
        #  self.is_valid(lines)
        self.lines = lines

        self.squares = []
        self.lines_to_squares(lines)

        self.columns = []
        self.lines_to_cols(lines)

        self.empty_cells = []  # index of all empty cells
        self.cells_to_fill()

        self.possibilities = {}  # key is cell index and value are all possible numbers
        self.possible_numbers()

    def is_valid(self, lines):
        for i in range(9):
            for j in range(9):
                if lines[i][j] > 9 or lines[i][j] < 0:
                    raise ValueError

    def __str__(self):
        sudoku = ""
        j = 0
        for line in self.lines:
            row = ""
            i = 0
            for num in line:
                i += 1
                row += str(num) + "  "
                if i % 3 == 0 and i != 9:
                    row += "|  "
            row += "\n"
            sudoku += row
            j += 1
            if j % 3 == 0 and j != 9:
                sudoku += "_______________________________\n\n"
        return sudoku

    def lines_to_squares(self, lines):
        self.squares = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                cur_square = [lines[i][j: j + 3]]
                cur_square.append(lines[i + 1][j: j + 3])
                cur_square.append(lines[i + 2][j: j + 3])
                self.squares.append(cur_square)

    def lines_to_cols(self, lines):
        """Transpose the sudoku"""
        self.columns = []
        for j in range(9):  # go through all columns
            row = []
            for i in range(9):  # go through all rows
                row.append(lines[i][j])
            self.columns.append(row)

    def is_in_line(self, number, line_number):
        if number in self.lines[line_number]:
            return True
        return False

    def is_in_column(self, number, col_number):
        if number in self.columns[col_number]:
            return True
        return False

    def is_in_square(self, number, square_num):
        for i in range(3):
            if number in self.squares[square_num][i]:
                return True
        return False

    def get_square_num(self, row, col):
        square_num = 0
        if row in [0, 1, 2] and col in [0, 1, 2]:
            square_num = 0
        elif row in [0, 1, 2] and col in [3, 4, 5]:
            square_num = 1
        elif row in [0, 1, 2] and col in [6, 7, 8]:
            square_num = 2
        elif row in [3, 4, 5] and col in [0, 1, 2]:
            square_num = 3
        elif row in [3, 4, 5] and col in [3, 4, 5]:
            square_num = 4
        elif row in [3, 4, 5] and col in [6, 7, 8]:
            square_num = 5
        elif row in [6, 7, 8] and col in [0, 1, 2]:
            square_num = 6
        elif row in [6, 7, 8] and col in [3, 4, 5]:
            square_num = 7
        elif row in [6, 7, 8] and col in [6, 7, 8]:
            square_num = 8

        return square_num

    def cells_to_fill(self):
        self.empty_cells = []
        for i in range(9):
            for j in range(9):
                if self.lines[i][j] == 0:
                    self.empty_cells.append((i, j))

    def only_possibility(self, cell, number):
        cur_square = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        square_num = self.get_square_num(cell[0], cell[1])
        for i in range(9):
            for j in range(9):
                if square_num == self.get_square_num(i, j) and self.lines[i][j] != 0:  # same square and not empty
                    cur_square[i % 3][j % 3] = 1

        if cell[0] % 3 == 0:
            if self.is_in_line(number, cell[0] + 1):
                for j in range(3):
                    cur_square[1][j] = 1
            if self.is_in_line(number, cell[0] + 2):
                for j in range(3):
                    cur_square[2][j] = 1

        if cell[0] % 3 == 1:
            if self.is_in_line(number, cell[0] + 1):
                for j in range(3):
                    cur_square[2][j] = 1
            if self.is_in_line(number, cell[0] - 1):
                for j in range(3):
                    cur_square[0][j] = 1

        if cell[0] % 3 == 2:
            if self.is_in_line(number, cell[0] - 1):
                for j in range(3):
                    cur_square[1][j] = 1
            if self.is_in_line(number, cell[0] - 2):
                for j in range(3):
                    cur_square[0][j] = 1

        if cell[1] % 3 == 0:
            if self.is_in_column(number, cell[1] + 1):
                for i in range(3):
                    cur_square[i][1] = 1
            if self.is_in_column(number, cell[1] + 2):
                for i in range(3):
                    cur_square[i][2] = 1

        if cell[1] % 3 == 1:
            if self.is_in_column(number, cell[1] + 1):
                for i in range(3):
                    cur_square[i][2] = 1
            if self.is_in_column(number, cell[1] - 1):
                for i in range(3):
                    cur_square[i][0] = 1

        if cell[1] % 3 == 2:
            if self.is_in_column(number, cell[1] - 1):
                for i in range(3):
                    cur_square[i][1] = 1
            if self.is_in_column(number, cell[1] - 2):
                for i in range(3):
                    cur_square[i][0] = 1

        counter = 0
        for row in cur_square:
            for num in row:
                if num == 0:
                    counter += 1

        return counter == 1  # if there is only 1 zero than it is the only possibility

    def possible_numbers(self):
        self.possibilities = {}
        for cell in self.empty_cells:
            possibilities = []
            square_num = self.get_square_num(cell[0], cell[1])
            for num in range(1, 10):
                if self.is_in_column(num, cell[1]) or self.is_in_line(num, cell[0]) \
                        or self.is_in_square(num, square_num):
                    continue
                else:
                    if self.only_possibility(cell, num):
                        possibilities = [num]
                        break
                    else:
                        possibilities.append(num)
            self.possibilities[cell] = possibilities

    def remove_from_filling_list(self):
        self.cells_to_fill()
        self.possible_numbers()

    def fill_cell(self, cell, number):
        self.lines[cell[0]][cell[1]] = number
        self.lines_to_squares(self.lines)
        self.lines_to_cols(self.lines)
        self.remove_from_filling_list()

    def unfill_cell(self, cell):
        self.lines[cell[0]][cell[1]] = 0
        self.lines_to_squares(self.lines)
        self.lines_to_cols(self.lines)
        self.remove_from_filling_list()

    def get_min_possibilities_cell(self):
        min_possibilities = 10
        min_cell = (0, 0)
        for cell in self.possibilities:
            num_possibilities = len(self.possibilities[cell])
            if num_possibilities < min_possibilities:
                min_possibilities = num_possibilities
                min_cell = cell

        return min_cell

    def must_guess(self):
        cell = self.get_min_possibilities_cell()
        if len(self.possibilities[cell]) == 1:
            return False
        if len(self.possibilities[cell]) == 0:
            return False
        return True

    def get_num_to_guess(self, min_cell, i):
        try:
            return self.possibilities[min_cell][i]
        except Exception:
            return False

    def correct_guess(self):
        for empty_cell in self.possibilities:
            if len(self.possibilities[empty_cell]) == 0:
                return False
        return True

    def solve(self, counter=0, memo=None, guessed_again=None):
        while self.empty_cells:
            if memo is None:
                memo = {}
            if guessed_again is None:
                guessed_again = {}
            cells_guessed = []
            if self.must_guess():
                cell_to_guess = self.get_min_possibilities_cell()
                if counter in guessed_again:
                    if guessed_again[counter] == cell_to_guess:
                        guessed_again.pop(counter)
                        # if counter != 0:
                        return False
                guessed_again[counter] = cell_to_guess

                for i in range(len(self.possibilities[cell_to_guess])):
                    num_to_guess = self.get_num_to_guess(cell_to_guess, i)
                    self.possibilities[cell_to_guess] = [num_to_guess]
                    good_guess = self.solve(counter + 1, memo, guessed_again)
                    if good_guess:
                        return True
                    else:
                        for wrong_cell in memo[counter]:
                            self.lines[wrong_cell[0]][wrong_cell[1]] = 0
                        self.__init__(self.lines)
                        memo.pop(counter)
                        cells_guessed = []

            if not self.correct_guess():  # for recursion call
                return False

            for empty_cell in self.possibilities:
                try:
                    if len(self.possibilities[empty_cell]) == 1:
                        self.fill_cell(empty_cell, self.possibilities[empty_cell][0])
                        cells_guessed.append(empty_cell)
                except KeyError:
                    memo[counter] = cells_guessed
                    return False
            if counter - 1 in memo:
                for cell in cells_guessed:
                    memo[counter - 1].append(cell)
            else:
                memo[counter - 1] = cells_guessed

        return True


def main(sudoku):
    s = Sudoku(sudoku)
    print("We started with this:")
    print(s)
    start_time = time.time()
    s.solve()
    elapsed_time = time.time() - start_time
    print("\n*****************************\n")

    print("Solution:")
    print(s)
    print("Solved in {} seconds".format(elapsed_time))

if __name__ == '__main__':
    sudoku = [[8, 0, 0, 0, 0, 1, 0, 5, 0], [0, 0, 3, 2, 0, 7, 0, 9, 0], [0, 0, 0, 0, 0, 0, 0, 3, 8],
              [0, 7, 0, 4, 6, 0, 0, 0, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 9, 2, 0, 8, 0],
              [2, 3, 0, 0, 0, 0, 0, 0, 0], [0, 8, 0, 9, 0, 3, 4, 0, 0], [0, 6, 0, 7, 0, 0, 0, 0, 0]]


    very_hard_sudoku = [[8, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 0, 0], [0, 7, 0, 0, 9, 0, 2, 0, 0],
                        [0, 5, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 4, 5, 7, 0, 0], [0, 0, 0, 1, 0, 0, 0, 3, 0],
                        [0, 0, 1, 0, 0, 0, 0, 6, 8], [0, 0, 8, 5, 0, 0, 0, 1, 0], [0, 9, 0, 0, 0, 0, 4, 0, 0]]

    main(sudoku=sudoku)

