import numpy as np

ROWS = 6
COLS = 7

#Funciones para el juego
def create_board():
    board = np.zeros((ROWS, COLS))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROWS-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
      #Verificar movimientos ganadores horizontales
      for c in range(COLS - 3):
          for r in range(ROWS - 3):
              if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                  return True
     #Verificar movimientos ganadores verticales
     for c in range(COLS):
         for r in range(ROWS - 3):
             if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                 return True

####################################################################################################################################

#Main

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
            if winning_move(board, 1):
                print("Jugador 1 gana")
                game_over = True
#Preguntar por el jugador 2
    else:
        col = int(input("Jugador 2, ingresa una columna: "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            print_board(board)
            if winning_move(board, 2):
                print("Jugador 2 gana")
                game_over = True
    turn += 1
    turn = turn % 2
