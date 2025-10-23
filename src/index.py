import pygame
import sys
import random

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

button_w, button_h = 200, 50
button_x = (ANCHO - button_w) // 2
button_y = GRID_SIZE + 40
button_rect = pygame.Rect(button_x, button_y, button_w, button_h)

# Fuente
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)

clock = pygame.time.Clock()

turn = 'player' 

def reset_board_and_choose_start():
    global board, turn
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    turn = random.choice(['player', 'machine'])

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
                if turn == 'player':
                    cell = board_cell_at_pos(mouse_pos)
                    if cell:
                        r, c = cell
                        if board[r][c] == 0:
                            board[r][c] = 1
                            turn = 'machine'

    pantalla.fill(BLANCO)
    draw_board(pantalla)
    draw_ui(pantalla)

    if turn == 'machine':
        draw_disabled_overlay(pantalla)

    pygame.display.flip()
    clock.tick(60)