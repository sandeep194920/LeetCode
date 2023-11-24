from collections import defaultdict


def is_valid_sudoku(board):
    row_tracker = defaultdict(list)
    col_tracker = defaultdict(list)
    square_tracker = defaultdict(list)

    for row_index in range(len(board)):
        for col_index in range(len(board[row_index])):

            if board[row_index][col_index] == '.':
                continue

            # Here we could actually combine the below if conditions into one if condition using 'or'
            # We will combine this in HashmapSingleIfCondition.py file
            if board[row_index][col_index] in row_tracker[str(row_index)]:
                return False
            row_tracker[str(row_index)].append(board[row_index][col_index])

            if board[row_index][col_index] in col_tracker[str(col_index)]:
                return False
            col_tracker[str(col_index)].append(board[row_index][col_index])

            if board[row_index][col_index] in square_tracker[str((row_index // 3, col_index // 3))]:
                return False
            square_tracker[str((row_index // 3, col_index // 3))].append(board[row_index][col_index])
    return True


sudoku_board = \
    [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(is_valid_sudoku(sudoku_board))
