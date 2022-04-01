import numpy as np

ROWS = 6
COLS = 7


def create_board():
    board = np.zeros((6, 7))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[5][col] == 0


def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


board = create_board()
game_over = False
turn = 0
print_board(board)
while not game_over:
#Preguntar por el jugador 1
    if turn == 0:
        col = int(input("Jugador 1, ingresa una columna: "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
            print_board(board)
#Preguntar por el jugador 2
    else:
        col = int(input("Jugador 2, ingresa una columna: "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            print_board(board)
    turn += 1
    turn = turn % 2
