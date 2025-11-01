import random

ROWS, COLS = 3, 3
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

turn = 'player'
game_over = False
winner = None

def check_win(board_arg, player):
    """Devuelve True si `player` (1 o 2) tiene línea ganadora."""
    for i in range(3):
        if all(board_arg[i][j] == player for j in range(3)): return True
        if all(board_arg[j][i] == player for j in range(3)): return True
    if all(board_arg[i][i] == player for i in range(3)): return True
    if all(board_arg[i][2-i] == player for i in range(3)): return True
    return False

def get_empty_positions(board_arg):
    """Devuelve lista de tuplas (r,c) de casillas vacías."""
    empties = []
    for r in range(3):
        for c in range(3):
            if board_arg[r][c] == 0:
                empties.append((r, c))
    return empties

def reset_board_and_choose_start():
    global board, turn, game_over, winner
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    turn = random.choice(['player', 'machine'])
    game_over = False
    winner = None
