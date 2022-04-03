import math

import numpy as np
import pygame
import sys
#Variables globales
ROWS = 6
COLS = 7
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
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
    for c in range(COLS):
        for r in range(ROWS):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()
####################################################################################################################################

#Se crea el tablero
board = create_board()
game_over = False
turn = 0

pygame.init()
pygame.display.set_caption('Conecta 4')
#Variables de pygame
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)
width = COLS * SQUARESIZE
height = (ROWS + 1) * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("monospace", 75)
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  # Salir del juego
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0] #Posicion del mouse en x
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update() #Actualizar pantalla
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            if turn == 0: #Turno del jugador 1
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))  #Columna donde se hace click
                if is_valid_location(board, col): #Verificar si la columna esta disponible
                    row = get_next_open_row(board, col) #Obtener la fila disponible
                    drop_piece(board, row, col, 1) #Tirar la ficha de jugador 1
                    draw_board(board)
                    if winning_move(board, 1): #Verificar si el jugador 1 gano
                        label = myfont.render("Jugador 1 gana", 4, RED)
                        screen.blit(label, (40, 10))
                        game_over = True
            else: #Turno del jugador 2
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))  # Columna donde se hace click
                if is_valid_location(board, col): #Verificar si la columna esta disponible
                    row = get_next_open_row(board, col) #Obtener la fila disponible
                    drop_piece(board, row, col, 2) #Tirar la ficha de jugador 2
                    draw_board(board)
                    if winning_move(board, 2): #Verificar si el jugador 2 gana
                        label = myfont.render("Jugador 2 gana", 4, RED)
                        screen.blit(label, (40, 10))
                        game_over = True
            turn += 1
            turn = turn % 2
            if game_over:  # Si el juego termino
                pygame.display.update()
                pygame.time.wait(3000)

