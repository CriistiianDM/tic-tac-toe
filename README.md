# Tic-Tac-Toe con Inteligencia Artificial

## 📋 Resumen

El videojuego Tic-Tac-Toe o Tres en Raya es un juego clásico en el cual dos jugadores compiten por alinear tres símbolos iguales en un tablero de 3x3. Este proyecto, desarrollado en Python, recrea este juego incorporando inteligencia artificial mediante los algoritmos de búsqueda **Minimax** y **Minimax con poda alfa-beta**, permitiendo la interacción humano vs máquina.

La representación de los estados del tablero se utiliza para analizar las posibles jugadas y determinar la mejor estrategia, haciendo que la IA sea un oponente formidable.

## 🎮 Características

- **Juego Clásico**: Implementación completa del juego Tres en Raya
- **Inteligencia Artificial Avanzada**: 
  - Algoritmo Minimax para decisiones óptimas
  - Minimax con poda Alfa-Beta para optimización de rendimiento
- **Modo Humano vs IA**: Juega contra la computadora
- **Análisis de Estados**: Representación y análisis de estados del tablero
- **Interfaz Intuitiva**: Interacción simple mediante consola

## 🧠 Algoritmos de IA

### Minimax

El algoritmo Minimax es una estrategia de decisión utilizada en juegos de suma cero. Funciona de la siguiente manera:

1. **Exploración del árbol de juego**: Explora todos los posibles movimientos futuros
2. **Evaluación de estados**: Asigna valores a los estados terminales
   - Victoria del jugador MAX: +10
   - Victoria del jugador MIN: -10
   - Empate: 0
3. **Propagación de valores**: Propaga los valores hacia arriba alternando entre maximizar y minimizar
4. **Selección de movimiento**: Elige el movimiento que maximiza el beneficio del jugador actual

**Ventajas:**
- Garantiza juego óptimo
- Encuentra la mejor jugada posible

**Desventajas:**
- Complejidad computacional alta en juegos grandes
- Explora todas las ramas del árbol

### Minimax con Poda Alfa-Beta

La poda alfa-beta es una optimización del algoritmo Minimax que reduce el número de nodos evaluados:

1. **Mantiene dos valores**:
   - **Alfa (α)**: Mejor valor garantizado para MAX
   - **Beta (β)**: Mejor valor garantizado para MIN
2. **Poda de ramas**: Elimina ramas que no pueden influir en la decisión final
3. **Condición de poda**: Cuando β ≤ α, se puede podar la rama

**Ventajas:**
- Reduce significativamente el número de nodos evaluados
- Mantiene la optimalidad del resultado
- Mejora el rendimiento hasta 50% en el mejor caso

**Comparación:**
```
Minimax sin poda: Evalúa ~549,945 estados en el peor caso
Minimax con poda alfa-beta: Evalúa ~18,297 estados en promedio
```

## 🎯 Representación del Tablero

El tablero se representa como una matriz de 3x3:

```python
tablero = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
```

- **'X'**: Representa al primer jugador
- **'O'**: Representa al segundo jugador o IA
- **' '**: Representa una casilla vacía

### Estados del Juego

El juego analiza los siguientes estados:
- **Estado inicial**: Tablero vacío
- **Estados intermedios**: Configuraciones durante el juego
- **Estados terminales**: Victoria, derrota o empate

## 🚀 Instalación

### Requisitos

- Python 3.7 o superior
- No requiere bibliotecas externas

### Clonar el Repositorio

```bash
git clone https://github.com/CriistiianDM/tic-tac-toe.git
cd tic-tac-toe
```

### Ejecutar el Juego

```bash
# crear venv (si no existe)
python -m venv venv

# si PowerShell bloquea scripts:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force

# activar
.\venv\Scripts\activate

# instalar requirements
pip install -r requirements.txt
```

## 💻 Uso

### Modo de Juego

### Seleccionar algoritmo (Minimax vs Alfa-Beta) vía variable de entorno

Ahora puedes elegir qué algoritmo usa la IA configurando la variable de entorno `USE_ALPHA`.

**Comportamiento**
- `USE_ALPHA=1`, `true`, `yes` → usa **Minimax con poda Alfa-Beta** (por defecto).
- `USE_ALPHA=0`, `false`, `no` → usa **Minimax recursivo**.

**Ejemplos (temporal, para la sesión actual)**

PowerShell:
```powershell
$env:USE_ALPHA = "0"   # usar minimax recursivo
py .\src\index.py

Al iniciar el juego, podrás elegir:

1. **Humano vs IA (Minimax)**: Juega contra la IA con algoritmo Minimax
2. **Humano vs IA (Alfa-Beta)**: Juega contra la IA optimizada con poda alfa-beta
3. **Humano vs Humano**: Modo para dos jugadores

### Cómo Jugar

1. El tablero se muestra numerado del 1 al 9:
   
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9

2. Ingresa el número de la casilla donde deseas colocar tu símbolo
3. La IA realizará su movimiento automáticamente
4. El juego continúa hasta que haya un ganador o empate

## 📁 Estructura del Proyecto

  tic-tac-toe/
  │
  ├── src/
  │   ├── application/           # Lógica principal del juego e IA
  │   ├── modules/               # Módulos auxiliares o reutilizables
  │   ├── view/                  # Interfaz gráfica (Pygame)
  │   ├── conteo_incorrectas.py  # Análisis o conteo de jugadas inválidas
  │   ├── index.py               # Punto de entrada principal del juego
  │   └── patrones_ganadores.py  # Comprobación de combinaciones ganadoras
  │
  ├── venv/                      # Entorno virtual de Python
  ├── .gitignore                 # Archivos y carpetas ignoradas por Git
  ├── README.md                  # Documentación del proyecto
  └── requirements.txt            # Dependencias necesarias del proyecto
```

## 🔬 Complejidad Algorítmica

### Minimax
- **Complejidad temporal**: O(b^d)
  - b = factor de ramificación (promedio ~5 movimientos por turno)
  - d = profundidad del árbol (~9 en Tic-Tac-Toe)
- **Complejidad espacial**: O(d)

### Minimax con Poda Alfa-Beta
- **Mejor caso**: O(b^(d/2))
- **Peor caso**: O(b^d)
- **Caso promedio**: Reduce evaluaciones entre 30-50%

## 🎓 Conceptos Clave

### Teoría de Juegos
- **Juego de suma cero**: Lo que gana un jugador, lo pierde el otro
- **Información perfecta**: Ambos jugadores conocen el estado completo
- **Determinístico**: No hay elementos aleatorios

### Estrategia Óptima
La IA implementa una estrategia óptima que:
- Garantiza la victoria si es posible
- Fuerza el empate cuando no puede ganar
- Nunca pierde si juega primero o segundo

## 📊 Análisis de Rendimiento

| Algoritmo | Nodos Evaluados | Tiempo Promedio | Memoria |
|-----------|----------------|-----------------|---------|
| Minimax | ~549,945 | ~2-3 segundos | O(d) |
| Alfa-Beta | ~18,297 | ~0.5-1 segundo | O(d) |

## 🛠️ Desarrollo

### Tecnologías Utilizadas

- **Lenguaje**: Python 3
- **Paradigma**: Programación orientada a objetos
- **Algoritmos**: Minimax, Poda Alfa-Beta

### Ejecutar Pruebas

```bash
python -m pytest tests/
```


## 📚 Referencias

- Russell, S., & Norvig, P. (2010). *Artificial Intelligence: A Modern Approach*
- Wikipedia: [Minimax Algorithm](https://en.wikipedia.org/wiki/Minimax)
- Wikipedia: [Alpha-Beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)


## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.


---
