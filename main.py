import numpy as np

ROWS = 6
COLS = 7


def create_board():
    board = np.zeros((6, 7))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

    def is_valid_location(board, col):
        return board[ROWS - 1][col] == 0

    def get_next_open_row(board, col):
        for r in range(ROWS):
            if board[r][col] == 0:
                return r

    def winning_move(board, piece):
        # Check horizontal locations for win
        for c in range(COLS - 3):
            for r in range(ROWS):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                    return True



board = create_board()


def print_board(board):
    print(np.flip(board, 0))


print_board(board)
game_over = False
turn = 0
# ask for player 1 input
while not game_over:
    if turn == 0:
        selection = input("Player 1, make your selection (0-6): ")
if is_valid_location(board, int(selection)):
    row = get_next_open_row(board, int(selection))
    drop_piece(board, row, int(selection), 1)

    # ask for player 2 input
    selection = input("Player 2, make your selection (0-6): ")
    if is_valid_location(board, int(selection)):
        row = get_next_open_row(board, int(selection))
        drop_piece(board, row, int(selection), 2)
    else:
        print("Invalid location")
    turn += 1
    turn = turn % 2
    print_board(board)
