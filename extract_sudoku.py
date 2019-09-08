import Sudoku

filename = r"C:\Users\Nadav\Desktop\p096_sudoku.txt"


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

sudokus = extract_sudoku(filename)



