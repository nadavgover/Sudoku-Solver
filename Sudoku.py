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
        # return squares  # 3D list

    def lines_to_cols(self, lines):
        """Transpose the sudoku"""
        self.columns = []
        #  sudoku = []
        for j in range(9):  # go through all columns
            row = []
            for i in range(9):  # go through all rows
                row.append(lines[i][j])
            #  sudoku.append(row)
            self.columns.append(row)
        #  return sudoku

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

    def get_index_in_square(self, square_num, row, col):
        line = 0
        column = 0
        if square_num == 0 or square_num == 1 or square_num == 2:
            line = row
        if square_num == 3 or square_num == 4 or square_num == 5:
            line = row + 3
        if square_num == 6 or square_num == 7 or square_num == 8:
            line = row + 6

        if square_num == 0 or square_num == 3 or square_num == 6:
            column = col
        if square_num == 1 or square_num == 4 or square_num == 7:
            column = col + 3
        if square_num == 2 or square_num == 5 or square_num == 8:
            column = col + 6

        return line, column

    def is_full_in_square(self, square_num):
        is_full = []
        for row in range(3):
            for col in range(3):
                if self.squares[square_num][row][col] != 0:
                    is_full.append((row, col))
        return is_full

    def lines_of_square_to_cols(self, square):
        """Transpose the sudoku"""
        sudoku = []
        for j in range(9):  # go through all columns
            row = []
            for i in range(9):  # go through all rows
                row.append(lines[i][j])
            sudoku.append(row)
        return sudoku

    def must_be_in_line_in_square(self):
        cur_square = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        square_count = -1
        row_count = -1
        col_count = -1
        for square in self.squares:
            square_count += 1
            # row_count = -1
            for row in square:
                row_count += 1
                col_count = -1
                for col in row:
                    col_count += 1
                    cur_cell = self.get_index_in_square(square_count, row_count, col_count)
                    # col_count += 1
                    for full_cell in self.is_full_in_square(square_count):
                        cur_square[full_cell[0]][full_cell[1]] = 1
                    if cur_cell in self.empty_cells:
                        for num in range(1, 10):
                            if not self.is_in_square(num, square_count):
                                if num not in self.possibilities[cur_cell]:
                                    cur_square[row_count][col_count] = 1
                                if self.is_in_line(num, cur_cell[0]):
                                    cur_square[row_count] = [1, 1, 1]
                                if self.is_in_column(num, cur_cell[1]):
                                    for i in range(3):
                                        cur_square[i][col_count] = 1
                                if cur_cell[1] % 3 == 0:
                                    if self.is_in_column(num, cur_cell[1] + 1):
                                        for i in range(3):
                                            cur_square[i][1] = 1
                                    if self.is_in_column(num, cur_cell[1] + 2):
                                        for i in range(3):
                                            cur_square[i][2] = 1

                                if cur_cell[1] % 3 == 1:
                                    if self.is_in_column(num, cur_cell[1] + 1):
                                        for i in range(3):
                                            cur_square[i][2] = 1
                                    if self.is_in_column(num, cur_cell[1] - 1):
                                        for i in range(3):
                                            cur_square[i][0] = 1

                                if cur_cell[1] % 3 == 2:
                                    if self.is_in_column(num, cur_cell[1] - 1):
                                        for i in range(3):
                                            cur_square[i][1] = 1
                                    if self.is_in_column(num, cur_cell[1] - 2):
                                        for i in range(3):
                                            cur_square[i][0] = 1

                                if 0 in cur_square[0] and 0 not in cur_square[1] and 0 not in cur_square[2]:
                                    square_num = self.get_square_num(cur_cell[0], cur_cell[1])
                                    for empty_cell in self.possibilities:
                                        if empty_cell[0] == cur_cell[0] and self.get_square_num(empty_cell[0], empty_cell[1]) != square_num:
                                            if num in self.possibilities[empty_cell]:
                                                self.possibilities[empty_cell].remove(num)

                                if 0 not in cur_square[0] and 0 in cur_square[1] and 0 not in cur_square[2]:
                                    square_num = self.get_square_num(cur_cell[0], cur_cell[1])
                                    for empty_cell in self.possibilities:
                                        if empty_cell[0] == cur_cell[0] and self.get_square_num(empty_cell[0], empty_cell[1]) != square_num:
                                            if num in self.possibilities[empty_cell]:
                                                self.possibilities[empty_cell].remove(num)

                                if 0 not in cur_square[0] and 0 not in cur_square[1] and 0 in cur_square[2]:
                                    square_num = self.get_square_num(cur_cell[0], cur_cell[1])
                                    for empty_cell in self.possibilities:
                                        if empty_cell[0] == cur_cell[0] and self.get_square_num(empty_cell[0], empty_cell[1]) != square_num:
                                            if num in self.possibilities[empty_cell]:
                                                self.possibilities[empty_cell].remove(num)

                                cur_square = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                                for full_cell in self.is_full_in_square(square_count):
                                    cur_square[full_cell[0]][full_cell[1]] = 1
                        if col_count == 2:
                            col_count = -1
            row_count = -1

    def must_be_in_col_in_square(self):
        cur_square = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        square_count = -1
        row_count = -1
        col_count = -1
        for square in self.squares:
            square_count += 1
            # row_count = -1
            for row in square:
                row_count += 1
                col_count = -1
                for col in row:
                    col_count += 1
                    cur_cell = self.get_index_in_square(square_count, row_count, col_count)
                    # col_count += 1
                    for full_cell in self.is_full_in_square(square_count):
                        cur_square[full_cell[0]][full_cell[1]] = 1
                    if cur_cell in self.empty_cells:
                        for num in range(1, 10):
                            if not self.is_in_square(num, square_count):
                                if num not in self.possibilities[cur_cell]:
                                    cur_square[row_count][col_count] = 1
                                if self.is_in_line(num, cur_cell[0]):
                                    cur_square[row_count] = [1, 1, 1]
                                if self.is_in_column(num, cur_cell[1]):
                                    for i in range(3):
                                        cur_square[i][col_count] = 1
                                if cur_cell[1] % 3 == 0:
                                    if self.is_in_column(num, cur_cell[1] + 1):
                                        for i in range(3):
                                            cur_square[i][1] = 1
                                    if self.is_in_column(num, cur_cell[1] + 2):
                                        for i in range(3):
                                            cur_square[i][2] = 1

                                if cur_cell[1] % 3 == 1:
                                    if self.is_in_column(num, cur_cell[1] + 1):
                                        for i in range(3):
                                            cur_square[i][2] = 1
                                    if self.is_in_column(num, cur_cell[1] - 1):
                                        for i in range(3):
                                            cur_square[i][0] = 1

                                if cur_cell[1] % 3 == 2:
                                    if self.is_in_column(num, cur_cell[1] - 1):
                                        for i in range(3):
                                            cur_square[i][1] = 1
                                    if self.is_in_column(num, cur_cell[1] - 2):
                                        for i in range(3):
                                            cur_square[i][0] = 1

                                transpose_square = self.lines_of_square_to_cols(cur_square)
                                if 0 in transpose_square[0] and 0 not in transpose_square[1] and 0 not in transpose_square[2]:
                                    square_num = self.get_square_num(cur_cell[0], cur_cell[1])
                                    for empty_cell in self.possibilities:
                                        if empty_cell[1] == cur_cell[1] and self.get_square_num(empty_cell[0], empty_cell[1]) != square_num:
                                            if num in self.possibilities[empty_cell]:
                                                self.possibilities[empty_cell].remove(num)

                                if 0 not in transpose_square[0] and 0 in transpose_square[1] and 0 not in transpose_square[2]:
                                    square_num = self.get_square_num(cur_cell[0], cur_cell[1])
                                    for empty_cell in self.possibilities:
                                        if empty_cell[1] == cur_cell[1] and self.get_square_num(empty_cell[0], empty_cell[1]) != square_num:
                                            if num in self.possibilities[empty_cell]:
                                                self.possibilities[empty_cell].remove(num)

                                if 0 not in transpose_square[0] and 0 not in transpose_square[1] and 0 in transpose_square[2]:
                                    square_num = self.get_square_num(cur_cell[0], cur_cell[1])
                                    for empty_cell in self.possibilities:
                                        if empty_cell[1] == cur_cell[1] and self.get_square_num(empty_cell[0], empty_cell[1]) != square_num:
                                            if num in self.possibilities[empty_cell]:
                                                self.possibilities[empty_cell].remove(num)

                                cur_square = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                                for full_cell in self.is_full_in_square(square_count):
                                    cur_square[full_cell[0]][full_cell[1]] = 1
                        if col_count == 2:
                            col_count = -1
            row_count = -1

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

    def count_empty_cells(self):
        counter = 0
        for i in range(9):
            for j in range(9):
                if self.lines[i][j] == 0:
                    counter += 1
        return counter

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
            # if not possibilities:  # no possibilities, sudoku can't be solved (probably wrong get_num_to_guess)
            #    return False
            self.possibilities[cell] = possibilities

        # return True

    def remove_from_filling_list(self):
        self.cells_to_fill()
        # self.empty_cells.remove(cell)
        # self.possibilities.pop(cell)
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

    def rec_solve(self):
        cell_to_guess = self.get_min_possibilities_cell()
        copy = Sudoku(self.lines)
        for i in range(len(self.possibilities[cell_to_guess])):
            self.__init__(copy.lines)
            # if not self.correct_guess():
            #    continue
            try:
                # if len(self.possibilities[cell_to_guess]) == 1:
                #    num_to_guess = self.get_num_to_guess(cell_to_guess, 0)
                # else:
                num_to_guess = self.get_num_to_guess(cell_to_guess, i)
                self.possibilities[cell_to_guess] = [num_to_guess]
            except KeyError:
                good_guess = self.solve()
                print good_guess
                if good_guess:
                    return True
                else:
                    self.__init__(copy.lines)

    def solve(self):
        while self.empty_cells != []:
            if self.must_guess():
                self.rec_solve()
            # if not self.correct_guess():  # for recursion call
            #    return False
            for empty_cell in self.possibilities:
                try:
                    # print len(self.empty_cells)
                    if len(self.possibilities[empty_cell]) == 1:
                        self.fill_cell(empty_cell, self.possibilities[empty_cell][0])
                except KeyError:
                    return False
                # print len(self.empty_cells)
                # print len(self.possibilities)
        # print self.empty_cells
        # print self.possibilities
        return True

    def solve1(self):
        # while self.empty_cells != []:
        while self.empty_cells:
            # copy = Sudoku(self.lines)
            if self.must_guess():
                cell_to_guess = self.get_min_possibilities_cell()
                copy = Sudoku(self.lines)
                for i in range(len(self.possibilities[cell_to_guess])):
                    # self.__init__(copy.lines)
                    if not self.correct_guess():  # for recursion call
                        self.unfill_cell(cell_to_guess)
                        return False
                    # if len(self.possibilities[cell_to_guess]) == 1:
                    #    num_to_guess = self.get_num_to_guess(cell_to_guess, 0)
                    # else:
                    num_to_guess = self.get_num_to_guess(cell_to_guess, i)
                    # if not num_to_guess:
                    #    return False
                    self.possibilities[cell_to_guess] = [num_to_guess]
                    good_guess = self.solve1()
                    # print good_guess
                    if good_guess:
                        return True
                    else:
                        self.__init__(copy.lines)
                        # self.unfill_cell(cell_to_guess)
            if not self.correct_guess():  # for recursion call
                return False
            for empty_cell in self.possibilities:
                # try:
                    # print len(self.empty_cells)
                if len(self.possibilities[empty_cell]) == 1:
                    self.fill_cell(empty_cell, self.possibilities[empty_cell][0])
                # except KeyError:
                #    return False
        return True

    def transpose(self,lines):
        """Transpose the sudoku"""
        sudoku = []
        for j in range(9):  # go through all columns
            row = []
            for i in range(9):  # go through all rows
                row.append(lines[i][j])
            sudoku.append(row)
        return sudoku

    # def solve2(self, copy=None):
    def solve2(self, counter=0, memo=None, guessed_again=None):
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
                    good_guess = self.solve2(counter + 1, memo, guessed_again)
                    if good_guess:
                        return True
                    else:
                        for wrong_cell in memo[counter]:
                            self.lines[wrong_cell[0]][wrong_cell[1]] = 0
                        self.__init__(self.lines)
                        memo.pop(counter)
                        cells_guessed = []

            if not self.correct_guess():  # for recursion call
                # memo[counter] = cells_guessed
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

lines0 = [[0, 7, 5, 0, 9, 0, 0, 0, 6], [0, 2, 3, 0, 8, 0, 0, 4, 0], [8, 0, 0, 0, 0, 3, 0, 0, 1],
          [5, 0, 0, 7, 0, 2, 0, 0, 0], [0, 4, 0, 8, 0, 6, 0, 2, 0], [0, 0, 0, 9, 0, 1, 0, 0, 3],
          [9, 0, 0, 4, 0, 0, 0, 0, 7], [0, 6, 0, 0, 7, 0, 5, 8, 0], [7, 0, 0, 0, 1, 0, 3, 9, 0]]

lines1 = [[1, 7, 5, 2, 9, 4, 8, 3, 6], [0, 2, 3, 0, 8, 0, 0, 4, 0], [8, 9, 0, 0, 0, 3, 0, 0, 1],
          [5, 0, 0, 7, 0, 2, 0, 0, 0], [0, 4, 0, 8, 0, 6, 0, 2, 0], [0, 8, 0, 9, 0, 1, 0, 0, 3],
          [9, 0, 0, 4, 0, 0, 0, 0, 7], [0, 6, 0, 0, 7, 9, 5, 8, 0], [7, 0, 0, 0, 1, 0, 3, 9, 0]]

lines2 = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]

lines3 = [[0, 0, 0, 0, 5, 0, 0, 0, 0], [9, 8, 0, 4, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 6],
          [0, 0, 0, 0, 0, 9, 0, 0, 0], [0, 3, 0, 0, 7, 0, 0, 6, 0], [0, 9, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 0, 6, 0, 0], [0, 0, 0, 5, 0, 0, 0, 0, 0]]

lines4 = [[8, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 0, 0], [0, 7, 0, 0, 9, 0, 2, 0, 0],
          [0, 5, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 4, 5, 7, 0, 0], [0, 0, 0, 1, 0, 0, 0, 3, 0],
          [0, 0, 1, 0, 0, 0, 0, 6, 8], [0, 0, 8, 5, 0, 0, 0, 1, 0], [0, 9, 0, 0, 0, 0, 4, 0, 0]]

lines5 = [[0, 6, 0, 1, 0, 4, 0, 5, 0], [0, 0, 8, 3, 0, 5, 6, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0, 1],
          [8, 0, 0, 4, 0, 7, 0, 0, 6], [0, 0, 6, 0, 0, 0, 3, 0, 0], [7, 0, 0, 9, 0, 1, 0, 0, 4],
          [5, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 7, 2, 0, 6, 9, 0, 0], [0, 4, 0, 5, 0, 8, 0, 7, 0]]

lines6 = [[7, 8, 0, 4, 0, 0, 1, 2, 0], [6, 0, 0, 0, 7, 5, 0, 0, 9], [0, 0, 0, 6, 0, 1, 0, 7, 8],
          [0, 0, 7, 0, 4, 0, 2, 6, 0], [0, 0, 1, 0, 5, 0, 9, 3, 0], [9, 0, 4, 0, 6, 0, 0, 0, 5],
          [0, 7, 0, 3, 0, 0, 0, 1, 2], [1, 2, 0, 0, 0, 7, 4, 0, 0], [0, 4, 9, 2, 0, 6, 0, 0, 7]]

lines7 = [[0, 6, 0, 0, 0, 8, 2, 5, 0], [0, 3, 0, 6, 7, 0, 0, 0, 0], [2, 0, 0, 0, 0, 3, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 7, 0, 2], [5, 0, 0, 0, 6, 0, 0, 0, 9], [9, 0, 4, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 7, 0, 0, 0, 0, 4], [0, 0, 0, 0, 4, 1, 0, 3, 0], [0, 5, 2, 8, 0, 0, 0, 1, 0]]

lines8 = [[5, 0, 0, 7, 8, 0, 0, 6, 0], [2, 0, 4, 0, 0, 0, 0, 0, 0], [0, 0, 6, 4, 0, 3, 1, 0, 0],
          [0, 0, 2, 0, 0, 8, 3, 9, 7], [0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 6, 7, 1, 0, 0, 2, 0, 0],
          [0, 0, 1, 9, 0, 6, 5, 0, 0], [0, 0, 0, 0, 0, 0, 9, 0, 6], [0, 8, 0, 0, 1, 5, 0, 0, 4]]

lines9 = [[0, 0, 0, 8, 0, 0, 3, 0, 0], [0, 0, 0, 4, 0, 0, 2, 0, 0], [8, 9, 3, 7, 0, 0, 5, 0, 0],
          [0, 0, 0, 0, 1, 0, 4, 9, 6], [0, 0, 0, 0, 0, 0, 0, 0, 0], [7, 1, 4, 0, 2, 0, 0, 0, 0],
          [0, 0, 9, 0, 0, 6, 7, 8, 5], [0, 0, 8, 0, 0, 5, 0, 0, 0], [0, 0, 2, 0, 0, 4, 0, 0, 0]]

lines10 = [[0, 0, 0, 0, 0, 5, 0, 6, 1], [0, 0, 4, 0, 7, 0, 0, 0, 5], [0, 9, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 5, 0, 0, 0, 3], [0, 4, 0, 2, 8, 6, 0, 7, 0], [5, 0, 0, 0, 4, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 2, 0], [7, 0, 0, 0, 2, 0, 9, 0, 0], [6, 1, 0, 4, 0, 0, 0, 0, 0]]

lines11 = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0],
           [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
           [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]

lines12 = [[2, 9, 5, 7, 0, 0, 8, 6, 0], [0, 3, 1, 8, 6, 5, 0, 2, 0], [8, 0, 6, 0, 0, 0, 0, 0, 0],
           [0, 0, 7, 0, 5, 0, 0, 0, 6], [0, 0, 0, 3, 8, 7, 0, 0, 0], [5, 0, 0, 0, 1, 6, 7, 0, 0],
           [0, 0, 0, 5, 0, 0, 1, 0, 9], [0, 2, 0, 6, 0, 0, 3, 5, 0], [0, 5, 4, 0, 0, 8, 6, 7, 2]]

lines13 = [[0, 8, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 9, 7, 3, 0, 0], [0, 0, 1, 4, 0, 0, 0, 5, 0],
           [0, 0, 8, 0, 0, 5, 0, 3, 0], [0, 7, 0, 0, 0, 0, 0, 4, 0], [0, 4, 0, 6, 0, 0, 8, 0, 0],
           [0, 5, 0, 0, 0, 3, 7, 0, 0], [0, 0, 3, 8, 1, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 1, 0]]

lines14 = [[0, 0, 0, 0, 8, 0, 0, 0, 0], [0, 1, 0, 7, 0, 6, 3, 0, 0], [0, 7, 0, 2, 0, 0, 5, 9, 0],
           [0, 0, 7, 0, 0, 0, 0, 3, 4], [0, 0, 6, 0, 2, 0, 9, 0, 0], [5, 2, 0, 0, 0, 0, 7, 0, 0],
           [0, 4, 3, 0, 0, 8, 0, 2, 0], [0, 0, 2, 6, 0, 9, 0, 5, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]]

lines15 = [[0, 3, 2, 0, 0, 0, 0, 0, 1], [6, 0, 0, 0, 1, 0, 9, 0, 0], [0, 0, 5, 4, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 1, 8, 3, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 1, 4, 3, 0, 0, 0, 0, 0],
           [8, 0, 0, 0, 0, 9, 4, 0, 0], [0, 0, 9, 0, 5, 0, 0, 0, 8], [3, 0, 0, 0, 0, 0, 1, 6, 0]]

lines16 = [[0, 0, 0, 0, 0, 6, 7, 0, 0], [0, 0, 2, 0, 3, 0, 0, 9, 0], [0, 0, 8, 0, 0, 1, 0, 0, 4],
           [6, 1, 0, 3, 0, 0, 0, 5, 9], [7, 0, 3, 0, 4, 0, 6, 0, 8], [8, 2, 0, 0, 0, 5, 0, 7, 3],
           [3, 0, 0, 1, 0, 0, 9, 0, 0], [0, 9, 0, 0, 7, 0, 8, 0, 0], [0, 0, 7, 5, 0, 0, 0, 0, 0]]

lines17 = [[0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 6, 0, 0, 0, 0, 3], [0, 7, 4, 0, 8, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 3, 0, 0, 2], [0, 8, 0, 0, 4, 0, 0, 1, 0], [6, 0, 0, 5, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 7, 8, 0], [5, 0, 0, 0, 0, 9, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 4, 0]]

lines18 = [[8, 0, 7, 4, 0, 1, 0, 0, 0], [3, 0, 0, 0, 0, 7, 9, 0, 2], [2, 0, 0, 0, 0, 0, 0, 8, 0],
           [6, 0, 5, 7, 4, 0, 0, 0, 0], [0, 0, 0, 3, 0, 5, 0, 0, 0], [0, 0, 0, 0, 6, 2, 5, 0, 4],
           [0, 1, 0, 0, 0, 0, 0, 0, 5], [5, 0, 3, 1, 0, 0, 0, 0, 8], [0, 0, 0, 5, 0, 6, 7, 0, 9]]

lines19 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

lines20 = [[0, 8, 0, 6, 0, 0, 0, 7, 0], [3, 0, 0, 1, 0, 0, 0, 0, 2], [0, 0, 4, 0, 3, 0, 6, 0, 0],
           [0, 0, 0, 0, 0, 6, 0, 5, 4], [0, 0, 8, 0, 2, 0, 9, 0, 0], [5, 1, 0, 7, 0, 0, 0, 0, 0],
           [0, 0, 2, 0, 7, 0, 4, 0, 0], [8, 0, 0, 0, 0, 3, 0, 0, 9], [0, 9, 0, 0, 0, 5, 0, 1, 0]]

lines21 = [[0, 0, 5, 2, 8, 0, 0, 0, 0], [0, 0, 0, 0, 0, 4, 1, 0, 0], [0, 0, 9, 0, 0, 0, 4, 0, 3],
           [9, 0, 0, 7, 0, 0, 0, 6, 0], [0, 8, 0, 0, 1, 0, 0, 4, 0], [0, 5, 0, 0, 0, 9, 0, 0, 1],
           [4, 0, 6, 0, 0, 0, 2, 0, 0], [0, 0, 7, 4, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 5, 6, 0, 0]]

lines22 = [[7, 9, 0, 0, 0, 3, 0, 0, 2], [0, 6, 0, 5, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2, 0, 0, 6],
           [0, 0, 0, 8, 0, 1, 0, 4, 0], [0, 0, 0, 0, 0, 0, 1, 0, 3], [5, 0, 0, 0, 2, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 7, 4], [0, 0, 1, 0, 0, 0, 0, 6, 5], [0, 0, 8, 0, 9, 7, 0, 0, 0]]

lines23 = [[0, 6, 0, 0, 0, 0, 0, 0, 0], [0, 1, 9, 6, 0, 0, 0, 0, 2], [0, 0, 7, 0, 0, 9, 0, 5, 0],
           [9, 0, 6, 0, 0, 4, 5, 0, 7], [0, 0, 0, 0, 3, 0, 0, 0, 0], [8, 0, 4, 7, 0, 0, 1, 0, 9],
           [0, 9, 0, 3, 0, 0, 6, 0, 0], [6, 0, 0, 0, 0, 5, 3, 8, 0], [0, 0, 0, 0, 0, 0, 0, 9, 0]]

lines24 = [[8, 0, 0, 0, 0, 1, 0, 5, 0], [0, 0, 3, 2, 0, 7, 0, 9, 0], [0, 0, 0, 0, 0, 0, 0, 3, 8],
           [0, 7, 0, 4, 6, 0, 0, 0, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 9, 2, 0, 8, 0],
           [2, 3, 0, 0, 0, 0, 0, 0, 0], [0, 8, 0, 9, 0, 3, 4, 0, 0], [0, 6, 0, 7, 0, 0, 0, 0, 0]]


import time

filename = r"C:\Users\Nadav\Desktop\p096_sudoku.txt"
filename1 = r"C:\Users\Nadav\Desktop\sudoku.csv"


def extract_sudoku(file):
    with open(file, "r") as sudoku_file:
        all_sudokus = []
        cur_sudoku = []
        counter = 0
        for line in sudoku_file:
            counter += 1
            row = []
            if counter == 50:
                all_sudokus.append(cur_sudoku)
            if line.startswith("Grid"):
                if counter != 1:
                    all_sudokus.append(cur_sudoku)
                cur_sudoku = []
                continue
            for number in line:
                if number != "\n":
                    row.append(int(number))
            cur_sudoku.append(row)

    return all_sudokus


def get_sudokus_or_solutions_from_csv(filename, i, num_sudokus):
    with open(filename, "r") as sud_file:
        count = 0
        all_sudokus = []
        cur_sudoku = []
        for line in sud_file:
            count += 1
            line = line.strip().split(",")
            if len(line[i]) != 81:  # not a sudoku for some reason (avoiding errors)
                count -= 1
                continue
            cur_line = []
            row_count = 0
            for num in line[i]:
                row_count += 1
                # if row_count % 10 != 0 or row_count == 0:
                if row_count > 0 and row_count < 10:
                    cur_line.append(int(num))
                else:
                    cur_sudoku.append(cur_line)
                    cur_line = []
                    cur_line.append(int(num))
                    row_count = 1
            cur_sudoku.append(cur_line)  # last line
            all_sudokus.append(cur_sudoku)
            cur_sudoku = []
            if count == num_sudokus:
                break

        return all_sudokus


def get_sudokus_csv(fname, number_sudokus=1000):
    sudokus = get_sudokus_or_solutions_from_csv(fname, i=0, num_sudokus=number_sudokus)
    solutions = get_sudokus_or_solutions_from_csv(fname, i=1, num_sudokus=number_sudokus)
    return sudokus, solutions
    # with open(filename, "r") as sud_file:
        # count = 0
        # all_sudokus = []
        # cur_sudoku = []
        # for line in sud_file:
        #     count += 1
        #     line = line.split(",")
        #     if len(line[0]) != 81:  # not a sudoku for some reason (avoiding errors)
        #         count -= 1
        #         continue
        #     cur_line = []
        #     row_count = 0
        #     for num in line[0]:
        #         row_count += 1
        #         # if row_count % 10 != 0 or row_count == 0:
        #         if row_count > 0 and row_count < 10:
        #             cur_line.append(int(num))
        #         else:
        #             cur_sudoku.append(cur_line)
        #             cur_line = []
        #             cur_line.append(int(num))
        #             row_count = 1
        #     cur_sudoku.append(cur_line)  # last line
        #     all_sudokus.append(cur_sudoku)
        #     cur_sudoku = []
        #     if count == num_sudokus:
        #         break
        #
        # return all_sudokus



number_of_sudokus_to_solve = 80000

# sudokus, solutions = get_sudokus_csv(filename1, number_of_sudokus_to_solve)
# # sudokus = extract_sudoku(filename)
# success = True
# start_time = time.time()
# for i in range(len(sudokus)):
#     s = Sudoku(sudokus[i])
#     s.solve2()
#     # sudokus[i] = s.lines
#     # if sudokus[i] != solutions[i]:
#     if s.lines != solutions[i]:
#         print i
#         success = False
#         break
#     # for line in s.lines:
#     #     if 0 in line:
#     #         success = False
#     #         break
# elapsed_time = time.time() - start_time
#
# if success:
#     print "Solved {} sudokus in {} seconds! {} minutes, {} hours.".format(len(sudokus), elapsed_time, elapsed_time/60, elapsed_time/3600)
#     print "Average of {} seconds per sudoku.".format(elapsed_time / len(sudokus))
#     print "Good job!"
# else:
#     print "Error occurred, not all sudokus were solved :("


s = Sudoku(lines24)
print "We started with this:"
print s
start_time = time.time()
s.solve2()
elapsed_time = time.time() - start_time
print "\n*****************************\n"

print "Solution:"
print s
print "Solved in {} seconds".format(elapsed_time)

