import pygame
import sys
import random
import copy

pygame.init()

ANCHO, ALTO = 600, 700 
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tic-Tac-Toe - Interfaz 3x3 (turnos)")


BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS_CLARO = (245, 245, 245)
GRIS = (200, 200, 200)
ROJO = (200, 30, 30)
AZUL = (30, 60, 200)
VERDE = (30, 150, 30)
TRANSPARENTE = (0, 0, 0, 120)

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

ROWS, COLS = 3, 3
GRID_SIZE = 600
grid_x = 0
grid_y = 0
cell_w = GRID_SIZE // COLS
cell_h = GRID_SIZE // ROWS
line_thickness = 6
padding = 20 

## Variuebles Globales
game_over = False
winner = None


button_w, button_h = 200, 50
button_x = (ANCHO - button_w) // 2
button_y = GRID_SIZE + 40
button_rect = pygame.Rect(button_x, button_y, button_w, button_h)

# Fuente
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)

clock = pygame.time.Clock()

turn = 'player' 

def check_win(board, player):
    """Devuelve True si `player` (1 o 2) tiene línea ganadora."""
    # filas/columnas
    for i in range(3):
        if all(board[i][j] == player for j in range(3)): return True
        if all(board[j][i] == player for j in range(3)): return True
    # diagonales
    if all(board[i][i] == player for i in range(3)): return True
    if all(board[i][2-i] == player for i in range(3)): return True
    return False

def get_empty_positions(board):
    """Devuelve lista de tuplas (r,c) de casillas vacías."""
    empties = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == 0:
                empties.append((r, c))
    return empties

def evaluate_position(board, pos, machine=2, player=1):
    """
    Simula colocar `machine` en pos (r,c) y devuelve:
      1  -> colocando allí la máquina gana inmediatamente
     -1  -> no gana inmediatamente y existe una respuesta inmediata del jugador que le hace ganar (pérdida)
      0  -> ni gana ni pierde inmediatamente (considerado empate/neutro)
    Nota: si pos ya ocupada devuelve 0 (se considera empate/neutro).
    """
    r, c = pos
    if board[r][c] != 0:
        return 0
    b = copy.deepcopy(board)
    b[r][c] = machine
    # 1 Gana Maquina
    if check_win(b, machine):
        return 1
    # si tablero lleno -> empate
    if not get_empty_positions(b):
        return 0
    # Pierde -1
    for (pr, pc) in get_empty_positions(b):
        b2 = copy.deepcopy(b)
        b2[pr][pc] = player
        if check_win(b2, player):
            return -1
    return 0

def minimax_recursive_choice(board, machine=2, player=1):
    """
    Devuelve la mejor jugada (r,c) usando minimax recursivo.
    Scores:  1 = victoria máquina, -1 = victoria jugador, 0 = empate.
    Se usa profundidad como criterio de desempate (prefiere ganar antes / perder después).
    """
    def minimax(is_maximizing):
        # terminales
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
                # prefer mayor score; si igual, prefer menor depth (ganar antes)
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
                # minimiza score; si igual, preferir mayor depth (hacer que la máquina tarde en ganar)
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

def reset_board_and_choose_start():
    global board, turn, game_over, winner
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    turn = random.choice(['player', 'machine'])
    game_over = False
    winner = None   

def draw_winner(surface):
    if not game_over:
        return
    if winner == 'EMPATE':
        txt = "EMPATE"
    else:
        txt = f"GANADOR: {winner}"
    s = font.render(txt, True, NEGRO)
    r = s.get_rect(center=(ANCHO // 2, GRID_SIZE // 2))
    surface.blit(s, r)
    
def draw_grid(surface):
    # fondo tablero
    for row in range(ROWS):
        for col in range(COLS):
            cell_rect = pygame.Rect(grid_x + col * cell_w, grid_y + row * cell_h, cell_w, cell_h)
            if (row + col) % 2 == 0:
                pygame.draw.rect(surface, GRIS_CLARO, cell_rect)
            else:
                pygame.draw.rect(surface, BLANCO, cell_rect)
    for i in range(1, COLS):
        x = grid_x + i * cell_w
        pygame.draw.line(surface, NEGRO, (x, grid_y), (x, grid_y + GRID_SIZE), line_thickness)
    for j in range(1, ROWS):
        y = grid_y + j * cell_h
        pygame.draw.line(surface, NEGRO, (grid_x, y), (grid_x + GRID_SIZE, y), line_thickness)

def draw_x(surface, rect):
    x1, y1 = rect.left + padding, rect.top + padding
    x2, y2 = rect.right - padding, rect.bottom - padding
    pygame.draw.line(surface, ROJO, (x1, y1), (x2, y2), 8)
    pygame.draw.line(surface, ROJO, (x1, y2), (x2, y1), 8)

def draw_o(surface, rect):
    center = rect.center
    radius = min(rect.width, rect.height) // 2 - padding
    pygame.draw.circle(surface, AZUL, center, radius, 8)

def draw_board(surface):
    draw_grid(surface)
    for row in range(ROWS):
        for col in range(COLS):
            val = board[row][col]
            cell_rect = pygame.Rect(grid_x + col * cell_w, grid_y + row * cell_h, cell_w, cell_h)
            if val == 1:
                draw_x(surface, cell_rect)
            elif val == 2:
                draw_o(surface, cell_rect)

def draw_ui(surface):
    turno_text = "Turno: JUGADOR (X)" if turn == 'player' else "Turno: MÁQUINA (O)"
    turno_color = VERDE if turn == 'player' else AZUL
    text_surf = font.render(turno_text, True, turno_color)
    text_rect = text_surf.get_rect(center=(ANCHO // 2, GRID_SIZE + 15))
    surface.blit(text_surf, text_rect)

    pygame.draw.rect(surface, GRIS, button_rect, border_radius=8)
    label = font.render("REFRESCAR", True, NEGRO)
    label_rect = label.get_rect(center=button_rect.center)
    surface.blit(label, label_rect)

    instr = small_font.render("Si es turno de MÁQUINA, clicks en tablero están deshabilitados.", True, (50,50,50))
    instr_rect = instr.get_rect(center=(ANCHO // 2, button_y + button_h + 20))
    surface.blit(instr, instr_rect)

def board_cell_at_pos(pos):
    x, y = pos
    if x < grid_x or x >= grid_x + GRID_SIZE or y < grid_y or y >= grid_y + GRID_SIZE:
        return None
    col = (x - grid_x) // cell_w
    row = (y - grid_y) // cell_h
    return int(row), int(col)

def draw_disabled_overlay(surface):
    overlay = pygame.Surface((GRID_SIZE, GRID_SIZE), pygame.SRCALPHA)
    overlay.fill(TRANSPARENTE)
    surface.blit(overlay, (grid_x, grid_y))
    aviso = font.render("TURNO MÁQUINA — CLICS DESACTIVADOS", True, (255,255,255))
    aviso_rect = aviso.get_rect(center=(ANCHO // 2, GRID_SIZE // 2))
    surface.blit(aviso, aviso_rect)

reset_board_and_choose_start()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            mouse_pos = evento.pos

            if button_rect.collidepoint(mouse_pos):
                reset_board_and_choose_start()
            else:
                if not game_over and turn == 'player':
                    cell = board_cell_at_pos(mouse_pos)
                    if cell:
                        r, c = cell
                        if board[r][c] == 0:
                            board[r][c] = 1
                            # comprobar si gana el jugador
                            if check_win(board, 1):
                                game_over = True
                                winner = 'JUGADOR'
                            elif not get_empty_positions(board):
                                game_over = True
                                winner = 'EMPATE'
                            else:
                                turn = 'machine'

    if turn == 'machine' and not game_over:
        draw_disabled_overlay(pantalla)
        move = minimax_recursive_choice(board)
        if move:
            r, c = move
            board[r][c] = 2
            if check_win(board, 2):
                game_over = True
                winner = 'MÁQUINA'
            elif not get_empty_positions(board):
                game_over = True
                winner = 'EMPATE'
            else:
                turn = 'player'
        else:
            game_over = True
            winner = 'EMPATE'

    pantalla.fill(BLANCO)
    draw_board(pantalla)
    draw_ui(pantalla)
    draw_winner(pantalla)
    pygame.display.flip()
    clock.tick(60)