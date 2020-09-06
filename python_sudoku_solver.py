"""
Takes the unsolved sudoku grid and returns it solved using a backtracking algorithm.
"""


"""
sampleGrid = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
"""

sudoku = [
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 8, 0, 0, 0, 7, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 5, 0, 0],
    [0, 7, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 4, 0],
    [0, 0, 5, 0, 0, 0, 6, 0, 3],
    [0, 9, 0, 4, 0, 0, 0, 7, 0],
    [0, 0, 6, 0, 0, 0, 0, 0, 0]
]


# prints the completed sudoku
def show_sudoku():
    for i in sudoku:
        print(i)


# algorithm for solving the input sudoku
def solve():
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for value in range(1, 10):
                    if check_value(i,j,value):
                        sudoku[i][j] = value
                        # call solve with the new value added, if later found to be wrong value, reset to 0
                        solve()
                        sudoku[i][j] = 0
                return
    show_sudoku()


# check if a given value can be placed at current position on grid
def check_value(i,j,value):
    # check row
    for x in range(9):
        if value == sudoku[i][x]:
            return False
    # check column
    for x in range(9):
        if value == sudoku[x][j]:
            return False
    # check square
    nRange = (i//3) * 3
    mRange = (j//3) * 3
    for n in range(nRange, nRange + 3):
        for m in range(mRange, mRange + 3):
                if value == sudoku[n][m]:
                    return False
    return True


solve()