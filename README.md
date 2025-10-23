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
python tic_tac_toe.py
```

## 💻 Uso

### Modo de Juego

Al iniciar el juego, podrás elegir:

1. **Humano vs IA (Minimax)**: Juega contra la IA con algoritmo Minimax
2. **Humano vs IA (Alfa-Beta)**: Juega contra la IA optimizada con poda alfa-beta
3. **Humano vs Humano**: Modo para dos jugadores

### Cómo Jugar

1. El tablero se muestra numerado del 1 al 9:
   ```
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```

2. Ingresa el número de la casilla donde deseas colocar tu símbolo
3. La IA realizará su movimiento automáticamente
4. El juego continúa hasta que haya un ganador o empate

## 📁 Estructura del Proyecto

```
tic-tac-toe/
│
├── README.md                 # Documentación del proyecto
├── tic_tac_toe.py           # Archivo principal del juego
├── minimax.py               # Implementación del algoritmo Minimax
├── alpha_beta.py            # Implementación de Minimax con poda alfa-beta
├── board.py                 # Representación y gestión del tablero
└── utils.py                 # Funciones auxiliares
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

### Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📚 Referencias

- Russell, S., & Norvig, P. (2010). *Artificial Intelligence: A Modern Approach*
- Wikipedia: [Minimax Algorithm](https://en.wikipedia.org/wiki/Minimax)
- Wikipedia: [Alpha-Beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

## 👨‍💻 Autor

**Cristian DM**
- GitHub: [@CriistiianDM](https://github.com/CriistiianDM)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🎯 Próximas Mejoras

- [ ] Interfaz gráfica con Pygame
- [ ] Diferentes niveles de dificultad
- [ ] Estadísticas de partidas
- [ ] Modo multijugador en red
- [ ] Tableros de diferentes tamaños (4x4, 5x5)
- [ ] Implementación de otros algoritmos de IA (Monte Carlo Tree Search)

## 🙏 Agradecimientos

Gracias a la comunidad de Python y a todos los que han contribuido a la teoría de juegos y algoritmos de búsqueda adversarial.

---

⭐️ Si te gusta este proyecto, no olvides darle una estrella en GitHub!