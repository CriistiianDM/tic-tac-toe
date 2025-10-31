import copy
import random

# Mostrar grafo en terminal para depuración
SHOW_GRAFO = True

# Definición del tablero
# 0 = vacío, 1 = "X", 2 = "O"
tablero = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Definición de patrones ganadores
# Cada patrón es una lista de coordenadas (fila, columna)
patrones_ganadores = [
    # Filas
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    # Columnas
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    # Diagonales
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]


def imprimir_tablero(t):
    """Imprime tablero con símbolos legibles."""
    simbolos = {0: ' ', 1: 'X', 2: 'O'}
    print('\nTablero:')
    for fila in t:
        print(' | '.join(simbolos[x] for x in fila))
    print('')


def evaluar_patrones(tab, jugador):
    """
    Devuelve un puntaje basado en qué tan cerca está el jugador de ganar.
    +3 -> victoria completa
    +2 -> dos en línea y un espacio libre
    +1 -> una marca en una línea libre
    0  -> línea bloqueada o sin marcas
    """
    puntaje = 0

    for patron in patrones_ganadores:
        valores = [tab[f][c] for (f, c) in patron]

        if valores.count(jugador) == 3:
            puntaje += 3  # victoria
        elif valores.count(jugador) == 2 and valores.count(0) == 1:
            puntaje += 2  # casi victoria
        elif valores.count(jugador) == 1 and valores.count(0) == 2:
            puntaje += 1  # posible línea futura
        # Si la línea contiene fichas del oponente, se ignora (bloqueada)

    return puntaje


def ganador(tab):
    # Devuelve 0 si no hay ganador, 1 o 2 si hay ganador
    for patron in patrones_ganadores:
        valores = [tab[f][c] for (f, c) in patron]
        if valores[0] != 0 and valores.count(valores[0]) == 3:
            return valores[0]
    return 0


def tablero_lleno(tab):
    return all(cell != 0 for row in tab for cell in row)


def elegir_mejor_movimiento(tab, jugador):
    """
    Construye un grafo de movimientos de primer nivel (una entrada por cada jugada legal).
    Cada nodo contiene la configuración resultante, la heurística para el jugador y para el
    oponente, y si la jugada produce una victoria inmediata.

    Luego selecciona la mejor jugada basándose en las heurísticas del grafo.
    """
    grafo = build_move_graph(tab, jugador)

    # Mostrar grafo si está activado
    if SHOW_GRAFO:
        print('\n--- Grafo de movimientos (primer nivel) ---')
        pretty_print_grafo(grafo)
        print('--- fin grafo ---\n')

    # Elegir el mejor movimiento según heurística del grafo
    mejores = []
    mejor_valor = None

    for mov, nodo in grafo.items():
        # valor simple: heur_jugador - heur_oponente, con prioridad a victorias
        valor = nodo['heur_jugador'] - nodo['heur_oponente']
        if nodo['winner'] == jugador:
            valor += 100

        # desempate por heurística absoluta del jugador
        if (mejor_valor is None) or (valor > mejor_valor):
            mejor_valor = valor
            mejores = [mov]
        elif valor == mejor_valor:
            mejores.append(mov)

    if not mejores:
        return None
    return random.choice(mejores)


def build_move_graph(tab, jugador):
    """
    Construye y devuelve un diccionario donde cada clave es una tupla (fila,col)
    que representa una jugada legal y el valor es un diccionario con:
      - state: tablero resultante (matriz)
      - heur_jugador: valor heurístico para 'jugador'
      - heur_oponente: valor heurístico para el oponente
      - winner: 0/1/2 si la jugada produce un ganador

    Esta función no explora más allá de profundidad 1; sirve como grafo de movimientos
    de primer nivel que luego puede usarse por algoritmos más complejos.
    """
    oponente = 1 if jugador == 2 else 2
    grafo = {}

    for i in range(3):
        for j in range(3):
            if tab[i][j] == 0:
                copia = copy.deepcopy(tab)
                copia[i][j] = jugador
                heur_j = evaluar_patrones(copia, jugador)
                heur_o = evaluar_patrones(copia, oponente)
                win = ganador(copia)

                grafo[(i, j)] = {
                    'state': copia,
                    'heur_jugador': heur_j,
                    'heur_oponente': heur_o,
                    'winner': win
                }

    return grafo


def pretty_print_grafo(grafo):
    # Imprime el grafo de movimientos para depuración
    for mov, nodo in grafo.items():
        i, j = mov
        print(f'Mov {mov}: heur_jugador={nodo["heur_jugador"]}, heur_oponente={nodo["heur_oponente"]}, winner={nodo["winner"]}')


def pedir_coordenada():
    # Pide coordenadas al usuario y valida entrada
    while True:
        try:
            a = int(input('elige la fila 0<=a<=2: '))
            b = int(input('elige la columna 0<=b<=2: '))
        except ValueError:
            print('Entrada no válida. Introduce números enteros entre 0 y 2.')
            continue

        if 0 <= a <= 2 and 0 <= b <= 2:
            return a, b
        else:
            print('Coordenadas fuera de rango. Intenta nuevamente.')


def main():
    global tablero

    print('Tic-Tac-Toe interactivo')
    print('1 = X (máquina), 2 = O (usuario)')

    while True:
        try:
            turno = int(input('Si escoges 1 empieza la máquina, si escoges 2 empiezas tú: '))
            if turno in (1, 2):
                break
        except ValueError:
            pass
        print('Introduce 1 o 2.')

    game_over = False

    while not game_over:
        imprimir_tablero(tablero)
        # Mostrar puntajes aproximados (heurísticos)
        punt_x = evaluar_patrones(tablero, 1)
        punt_o = evaluar_patrones(tablero, 2)
        print(f'Heurística -> X: {punt_x}  O: {punt_o}\n')

        if turno == 1:
            print('Turno: Máquina (X)')
            mov = elegir_mejor_movimiento(tablero, 1)
            if mov is None:
                # Ningún movimiento posible (tablero lleno)
                print('No hay movimientos posibles.')
                break
            a, b = mov
            print(f'Máquina elige: fila {a}, columna {b}')
            tablero[a][b] = 1

            g = ganador(tablero)
            if g != 0:
                imprimir_tablero(tablero)
                print(f'Gana el jugador {g} ({"X" if g==1 else "O"})')
                break

            if tablero_lleno(tablero):
                imprimir_tablero(tablero)
                print('Empate (tablero lleno).')
                break

            turno = 2
        else:
            print('Turno: Usuario (O)')
            while True:
                a, b = pedir_coordenada()
                if tablero[a][b] != 0:
                    print('La casilla ya está ocupada. Elige otra.')
                else:
                    tablero[a][b] = 2
                    break

            g = ganador(tablero)
            if g != 0:
                imprimir_tablero(tablero)
                print(f'Gana el jugador {g} ({"X" if g==1 else "O"})')
                break

            if tablero_lleno(tablero):
                imprimir_tablero(tablero)
                print('Empate (tablero lleno).')
                break

            turno = 1


if __name__ == '__main__':
    main()