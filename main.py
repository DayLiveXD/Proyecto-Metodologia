import numpy as np
import pygame
import sys

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
     #Verificar movimientos ganadores positivos diagonales
      for c in range(COLS - 3):
                for r in range(ROWS - 3):
                    if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                        return True
      #Verificar movimientos ganadores negativos diagonales
      for c in range(COLS - 3):
                for r in range(3, ROWS):
                    if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                        return True

def draw_board(board):
    for c in range(COLS):
        for r in range(ROWS):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

####################################################################################################################################
#Main

board = create_board()
game_over = False
turn = 0
print_board(board)
pygame.init()

SQUARESIZE = 100

width = COLS * SQUARESIZE
height = (ROWS + 1) * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            continue

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
