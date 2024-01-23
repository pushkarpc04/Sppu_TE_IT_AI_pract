#Implement n-queens problem using Hill-climbing / simulated annealing / A* algorithm etc.
#Write a program for Water jug problem / Towers of Hano

import random

def is_valid(board):
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                return False
    return True

def calculate_heuristic(board):
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def hill_climbing(n):
    current_board = [random.randint(0, n-1) for _ in range(n)]
    current_heuristic = calculate_heuristic(current_board)

    while current_heuristic > 0:
        next_board = list(current_board)
        for i in range(n):
            for j in range(n):
                if current_board[i] != j:
                    next_board[i] = j
                    next_heuristic = calculate_heuristic(next_board)
                    if next_heuristic < current_heuristic:
                        current_board = list(next_board)
                        current_heuristic = next_heuristic

        if current_heuristic == calculate_heuristic(current_board):
            break

    return current_board

# Example usage
n = 8
solution = hill_climbing(n)
print("N-Queens Solution:", solution)
