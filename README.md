<img width="1414" height="734" alt="Portada de cuaderno digital de trabajo práctico ilustrativo violeta" src="https://github.com/user-attachments/assets/044076d8-4eb9-47d0-a5bb-8572db1f0f5b" />

## ¿Qué hace esta app?

Imagina que tienes un robot y lo metes en un laberinto. ¿Cómo sabe el robot por dónde ir? ¿Cómo encuentra el camino más corto? ¿Qué pasa si hay obstáculos?

**El proyecto** te muestra eso, paso a paso, con colores y explicaciones en pantalla. Puedes ver exactamente qué está pensando cada algoritmo en cada momento: qué celdas ya exploró, cuál está visitando ahora, y por dónde va a continuar.

## Instalación rápida

```bash
# 1. Clona el repositorio

# 2. Instala Streamlit (solo la primera vez)
pip install streamlit

# 3. Ejecuta la app
streamlit run app.py
```

Abre tu navegador en **http://localhost:8501** y ya está.

---

## Cómo se usa

La app tiene **4 pestañas** en la barra inferior (como cualquier app de celular):
<div align="center">

| Pestaña          | Descripción                                          |
| ---------------- | ---------------------------------------------------- |
| **⌂ Inicio**     | Pantalla principal. Toca una categoría para empezar. |
| **⬡ Algoritmos** | Elige qué algoritmo ver y configura las opciones.    |
| **◈ Visualizar** | Arrastra el slider para ver cada paso del algoritmo. |
| **◎ Info**       | Descripción rápida de todos los algoritmos.          |

</div>

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/436b9d72-09cc-43b9-a9f9-da798acd4ff5"
    alt="Captura de pantalla"
    width="350"
  />
</p>

**Pasos:**
1. Toca una categoría en **Inicio** (o ve a **Algoritmos**)
2. Selecciona el algoritmo que quieres
3. Presiona **▶ Ejecutar**
4. Ve a **Visualizar** y arrastra el slider de izquierda a derecha

---

## Las 4 categorías

---

### 1. Búsqueda No Informada — Laberinto Frozen Lake

**El problema:** Un robot debe ir de `S` (inicio) hasta `G` (meta) en un laberinto de 4×4, sin caer en los hoyos `H`.

```
S  F  F  F
F  H  F  H
F  F  F  F
H  F  F  G
```

- **S** = Inicio (esquina arriba-izquierda)
- **F** = Frozen / Seguro (puede pasar)
- **H** = Hoyo (¡peligro! no puede pasar)
- **G** = Meta (esquina abajo-derecha)

**Algoritmos incluidos:**

#### BFS — Búsqueda en Amplitud
El robot explora como si lanzara ondas en el agua: primero todas las celdas a 1 paso, luego a 2 pasos, luego a 3...

- ✅ **Ventaja:** Siempre encuentra el camino MÁS CORTO
- ❌ **Desventaja:** Usa mucha memoria
- 📦 **Estructura:** Cola FIFO (el primero en entrar es el primero en salir)

#### DFS — Búsqueda en Profundidad
El robot elige un camino y lo sigue hasta el fondo antes de retroceder. Como explorar una cueva siguiendo siempre la pared derecha.

- ✅ **Ventaja:** Usa muy poca memoria
- ❌ **Desventaja:** No garantiza el camino más corto
- 📦 **Estructura:** Pila LIFO (el último en entrar es el primero en salir)

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/c65af740-bbbe-4623-ae11-c5a3dad57d57"
    alt="Captura de pantalla 1"
    width="400"
  />
</p>

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/045c0e45-6347-454b-a118-e1e646f71830"
    alt="Captura de pantalla 2"
    width="400"
  />
</p>


---

### 2. Búsqueda Informada — Manhattan Gridworld (4×7)

**El problema:** Ir de `I=(3,0)` hasta `F=(1,4)` en un grid de 4 filas × 7 columnas con paredes (`X`).

```
(0,0)  X   (0,2) (0,3) (0,4) (0,5) (0,6)
h=5         h=3   h=2   h=1   h=2   h=3

(1,0)(1,1)(1,2)  X    F    X    X
h=4  h=3  h=2        META

(2,0)  X  (2,2)  X  (2,4) (2,5) (2,6)
h=5        h=3       h=1   h=2   h=3

 I    X   (3,2)(3,3)(3,4)(3,5)(3,6)
h=6        h=4  h=3  h=2  h=3  h=4
```

**La heurística Manhattan:** `h(n) = |fila_actual − fila_meta| + |col_actual − col_meta|`

Ejemplo: desde `(3,0)` hasta `(1,4)`: `h = |3-1| + |0-4| = 2 + 4 = **6**`

Es la distancia en pasos rectos, como si no hubiera paredes. Siempre es menor o igual al costo real → la heurística nunca miente.

#### A* — A Estrella
Usa `f(n) = g(n) + h(n)`:
- `g(n)` = pasos reales dados desde el inicio
- `h(n)` = estimación de pasos hasta la meta (Manhattan)
- `f(n)` = costo total estimado

Siempre expande el nodo con menor `f(n)`. La app muestra en cada paso las listas **OPEN** (nodos pendientes) y **CLOSED** (ya explorados).

- ✅ **Ventaja:** Óptimo y completo
- ❌ **Desventaja:** Usa más memoria que Greedy

#### Greedy Best-First
Solo usa `h(n)`. Va siempre hacia donde parece más cerca de la meta, sin importar cuántos pasos ya dio. Más impaciente que A*.

- ✅ **Ventaja:** Generalmente más rápido
- ❌ **Desventaja:** Puede no encontrar el camino más corto
<p align="center">
  <img
    src="https://github.com/user-attachments/assets/d529c622-f9fd-4454-ab1e-4b82526c5e3e"
    alt="Captura de pantalla 1"
    width="400"
  />
</p>

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/17d0b2c4-be76-4dde-9374-275a8185cec8"
    alt="Captura de pantalla 2"
    width="400"
  />
</p>

---

### 3. Búsqueda Local — Problema de las 8 Reinas

**El problema:** Colocar 8 reinas en un tablero de ajedrez 8×8 sin que ninguna ataque a otra.

**Representación:** `[3, 6, 2, 7, 1, 4, 0, 5]`
- Índice = fila (0 a 7)
- Valor = columna donde está la reina en esa fila

**Dos reinas se atacan si:**
- Están en la misma columna: `estado[i] == estado[j]`
- Están en la misma diagonal: `|estado[i] − estado[j]| == |i − j|`

**Meta:** llegar a **0 conflictos** (ningún par de reinas se ataca).

**Colores en el tablero:**
- 🟢 Q verde = sin conflicto
- 🔴 Q roja = en conflicto con otra reina
- 🔵 Q azul = la reina que acaba de moverse

#### Hill Climbing — Ascenso de Colina
Evalúa TODOS los movimientos posibles (mover cualquier reina a otra columna) y elige el que más reduce los conflictos.

- ✅ **Ventaja:** Simple y rápido
- ❌ **Desventaja:** Se atasca en óptimos locales (ningún vecino mejora pero aún hay conflictos)

#### Simulated Annealing — Recocido Simulado
Como Hill Climbing pero a veces acepta movimientos peores para escapar de callejones sin salida. La probabilidad de aceptar un movimiento malo es: `e^(−delta/T)`

La temperatura `T` empieza alta (acepta casi todo) y baja gradualmente hasta que solo acepta mejoras.

- ✅ **Ventaja:** Puede escapar de óptimos locales
- ❌ **Desventaja:** Más lento, parámetros críticos

> **En el modo Comparación:** ambos algoritmos usan el mismo estado inicial para que la comparación sea justa.

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/b9c8bfce-6aca-45a5-92c5-fbb68dab317f"
    alt="Captura de pantalla 1"
    width="400"
  />
</p>

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/d52a657d-463b-4236-9be2-7697acfa57ac"
    alt="Captura de pantalla 2"
    width="400"
  />
</p>



---

### 4. Búsqueda Adversaria — Tic-Tac-Toe (Gato)

**El problema:** Jugar al Gato de forma perfecta.

```
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

- **X** = Computadora = MAX (quiere ganar)
- **O** = Usuario = MIN (quiere evitar que X gane)

**Se gana con 3 en línea:**
- ↔ Horizontal (filas 0-1-2, 3-4-5, 6-7-8)
- ↕ Vertical (columnas 0-3-6, 1-4-7, 2-5-8)
- ↗ Diagonal (0-4-8 y 2-4-6)

**Evaluación de puntajes:**

<div align="center">

| Puntaje | Significado |
|---------|-------------|
| +9 | X GANA AHORA (3 en línea directa) |
| +7 | X forzará 3 en línea en 3 turnos |
| 0 | Empate con juego perfecto |
| -7 | O forzará 3 en línea en 3 turnos |
| -9 | O GANA AHORA |

</div>

#### Minimax
X explora TODOS los futuros posibles del juego. Para cada jugada que puede hacer X, calcula qué haría O de forma perfecta, qué haría X después, y así hasta el final del juego.

- ✅ **Ventaja:** X nunca pierde
- ❌ **Desventaja:** Lento en juegos con muchas posibilidades

#### Alpha-Beta Pruning
Exactamente igual que Minimax pero más inteligente. Lleva dos límites:
- `alpha` = lo mejor que X puede garantizar
- `beta` = lo mejor que O puede garantizar

Si `beta ≤ alpha`, esa rama nunca importará → se poda y no se explora.

- ✅ **Ventaja:** Mismo resultado que Minimax, muchos menos nodos evaluados
- ❌ **Desventaja:** Más complejo de implementar

#### Modo Juego Interactivo

Activa "Jugar contra la computadora":
1. La computadora (X) abre en el centro (posición 4)
2. Toca cualquier celda vacía para jugar como O
3. La computadora responde y te muestra su análisis
4. **La computadora NUNCA pierde** (Minimax lo garantiza)

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/1464522e-3308-4e9b-a838-ea755b2fbb15"
    alt="Captura de pantalla"
    width="400"
  />
</p>


---

## Modo Comparación

Activa "Comparar" en la pestaña Algoritmos para ver dos algoritmos al mismo tiempo:
- Slider compartido: avanzas ambos a la vez
- Visualización lado a lado
- Al final: tabla comparativa con ganador
<p align="center">
  <img
    src="https://github.com/user-attachments/assets/b45dfd85-2c7b-455e-bf9f-1cf04eb5b5f4"
    alt="Captura de pantalla 1"
    width="400"
  />
</p>

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/4f962701-ae7e-48be-81f4-52e6e4b5b340"
    alt="Captura de pantalla 2"
    width="400"
  />
</p>



---

## Estructura del proyecto

```
Proyecto/
├── app.py                    # Interfaz completa
├── busqueda_no_informada.py  # BFS, DFS → Frozen Lake 4×4
├── busqueda_informada.py     # A*, Greedy → Manhattan Gridworld 4×7
├── busqueda_local.py         # Hill Climbing, SA → 8 Reinas
└── busqueda_adversaria.py    # Minimax, Alpha-Beta → Tic-Tac-Toe
```

---

## Explicación Rápida

- **BFS** = explorar todo alrededor antes de ir lejos (como un radar)
- **DFS** = seguir un camino hasta el final y regresar si no funciona (como una lombriz)
- **A\*** = usar un mapa para no explorar lugares inútiles
- **Greedy** = siempre ir hacia donde huele más la meta, sin importar si el camino es bueno
- **Hill Climbing** = siempre subir la colina, pero te puedes quedar atascado en una loma pequeña
- **Simulated Annealing** = a veces bajar la loma para luego subir más alto
- **Minimax** = pensar todos los movimientos del juego antes de hacer uno
- **Alpha-Beta** = Minimax pero más listo: ignora los movimientos que claramente no importan


---

*Proyecto Búsqueda IA — Hecho con Python + Streamlit* 

---

**Autores:**
**María Fernanda García Hernández** ([@MaferGH](https://github.com/MaferGH)) • **Abraham Mora Olvera** ([@AbrahamM0](https://github.com/AbrahamM0))

---

<img width="2000" height="965" alt="b2b-Photoroom" src="https://github.com/user-attachments/assets/bef7e492-1ca3-4112-8d26-249bb7d83204" />

