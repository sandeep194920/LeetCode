from collections import defaultdict


def is_valid_sudoku(board):
    row_tracker = defaultdict(list)
    col_tracker = defaultdict(list)
    square_tracker = defaultdict(list)

    for row_index in range(len(board)):
        for col_index in range(len(board[row_index])):

            if board[row_index][col_index] == '.':
                continue

            # Combining all if conditions into a single if condition
            # (we can write it separately as well as implemented in Hashmap.py)

            if board[row_index][col_index] in row_tracker[str(row_index)] \
                    or board[row_index][col_index] in col_tracker[
                str(col_index)] \
                    or board[row_index][col_index] in square_tracker[str((row_index // 3, col_index // 3))]:
                return False
            row_tracker[str(row_index)].append(board[row_index][col_index])
            col_tracker[str(col_index)].append(board[row_index][col_index])
            square_tracker[str((row_index // 3, col_index // 3))].append(board[row_index][col_index])
    return True


sudoku_board = \
    [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(is_valid_sudoku(sudoku_board))
