#Write a program for the Tic-Tac-Toe game.\

import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 300, 300
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def draw_grid():
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 2)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)

def draw_symbol(row, col, symbol):
    font = pygame.font.Font(None, 100)
    text = font.render(symbol, True, BLACK)
    text_rect = text.get_rect(center=((col * CELL_SIZE) + CELL_SIZE // 2, (row * CELL_SIZE) + CELL_SIZE // 2))
    screen.blit(text, text_rect)

def check_winner(symbol):
    for i in range(GRID_SIZE):
        if all(board[i][j] == symbol for j in range(GRID_SIZE)) or all(board[j][i] == symbol for j in range(GRID_SIZE)):
            return True
    if all(board[i][i] == symbol for i in range(GRID_SIZE)) or all(board[i][GRID_SIZE - 1 - i] == symbol for i in range(GRID_SIZE)):
        return True
    return False

def is_board_full():
    return all(board[i][j] != ' ' for i in range(GRID_SIZE) for j in range(GRID_SIZE))

def reset_game():
    global board
    board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def computer_move():
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if board[i][j] == ' ']
    return random.choice(empty_cells) if empty_cells else None

running = True

player_symbol = input("Do you want to play as X or O? ").upper()
if player_symbol not in ['X', 'O']:
    print("Invalid choice. Defaulting to 'X'.")
    player_symbol = 'X'

computer_symbol = 'O' if player_symbol == 'X' else 'X'
turn = 'X' if player_symbol == 'X' else 'O'

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if turn == player_symbol:
                mouseX, mouseY = event.pos
                clicked_row = mouseY // CELL_SIZE
                clicked_col = mouseX // CELL_SIZE

                if 0 <= clicked_row < GRID_SIZE and 0 <= clicked_col < GRID_SIZE and board[clicked_row][clicked_col] == ' ':
                    board[clicked_row][clicked_col] = turn

                    if check_winner(turn):
                        print(f'{turn} wins!')
                        reset_game()

                    elif is_board_full():
                        print("It's a draw!")
                        reset_game()

                    turn = computer_symbol

    if turn == computer_symbol:
        computer_move_pos = computer_move()
        if computer_move_pos:
            board[computer_move_pos[0]][computer_move_pos[1]] = computer_symbol

            if check_winner(turn):
                print(f'{turn} wins!')
                reset_game()

            elif is_board_full():
                print("It's a draw!")
                reset_game()

            turn = player_symbol

    screen.fill(WHITE)
    draw_grid()

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] != ' ':
                draw_symbol(row, col, board[row][col])

    pygame.display.flip()

pygame.quit()
sys.exit()
