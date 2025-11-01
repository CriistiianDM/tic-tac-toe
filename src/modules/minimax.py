from application.core import check_win, get_empty_positions

def minimax_recursive_choice(board, machine=2, player=1):
    """
    Devuelve la mejor jugada (r,c) usando minimax recursivo.
    Scores:  1 = victoria máquina, -1 = victoria jugador, 0 = empate.
    Se usa profundidad como criterio de desempate.
    """
    def minimax(is_maximizing):
        if check_win(board, machine):
            return 1, 0
        if check_win(board, player):
            return -1, 0
        empties = get_empty_positions(board)
        if not empties:
            return 0, 0

        if is_maximizing:
            best_score, best_depth = -2, 999
            for (r, c) in empties:
                board[r][c] = machine
                score, depth = minimax(False)
                board[r][c] = 0
                depth += 1
                if (score > best_score) or (score == best_score and depth < best_depth):
                    best_score, best_depth = score, depth
            return best_score, best_depth
        else:
            best_score, best_depth = 2, 999
            for (r, c) in empties:
                board[r][c] = player
                score, depth = minimax(True)
                board[r][c] = 0
                depth += 1
                if (score < best_score) or (score == best_score and depth < best_depth):
                    best_score, best_depth = score, depth
            return best_score, best_depth

    best_move = None
    best_score, best_depth = -2, 999
    for (r, c) in get_empty_positions(board):
        board[r][c] = machine
        score, depth = minimax(False)
        board[r][c] = 0
        depth += 1
        if (score > best_score) or (score == best_score and depth < best_depth):
            best_score, best_depth, best_move = score, depth, (r, c)
            if best_score == 1:
                break
    return best_move