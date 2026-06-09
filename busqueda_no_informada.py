"""
Búsqueda No Informada - Laberinto tipo Frozen Lake
Algoritmos: BFS, DFS

Mapa:
  S  F  F  F
  F  H  F  H
  F  F  F  F
  H  F  F  G

S = Inicio, F = Frozen (seguro), H = Hoyo (peligroso), G = Meta
"""

from collections import deque
import heapq

# 0 = celda, 1 = hoyo
LABERINTO = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
]
INICIO = (0, 0)
META   = (3, 3)
FILAS  = 4
COLS   = 4


def celda_valida(fila, col):
    """Verifica si una celda existe y no es un hoyo."""
    if fila < 0 or fila >= FILAS:
        return False
    if col < 0 or col >= COLS:
        return False
    if LABERINTO[fila][col] == 1:
        return False
    return True


def obtener_vecinos(celda):
    """Devuelve las celdas accesibles desde la celda actual (4 direcciones)."""
    fila, col = celda
    vecinos = []
    # Arriba
    if celda_valida(fila - 1, col):
        vecinos.append((fila - 1, col))
    # Abajo
    if celda_valida(fila + 1, col):
        vecinos.append((fila + 1, col))
    # Izquierda
    if celda_valida(fila, col - 1):
        vecinos.append((fila, col - 1))
    # Derecha
    if celda_valida(fila, col + 1):
        vecinos.append((fila, col + 1))
    return vecinos


def reconstruir_camino(padres, nodo):
    """Sigue los padres hacia atrás para obtener el camino completo."""
    camino = []
    actual = nodo
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    camino.reverse()
    return camino

# BFS — Búsqueda en Amplitud

def bfs():
    pasos  = []
    cola   = deque()
    padres = {}
    visitados = set()
    cola.append(INICIO)
    visitados.add(INICIO)
    padres[INICIO] = None

    pasos.append({
        "tipo":      "inicio",
        "celda":     INICIO,
        "visitados": set(visitados),
        "frontera":  list(cola),
        "mensaje":   (
            f"BFS inicia en {INICIO}\n"
            f"Se agrega {INICIO} a la cola\n"
            f"Meta: {META}"
        )
    })

    while len(cola) > 0:
        actual = cola.popleft()

        if actual == META:
            camino = reconstruir_camino(padres, actual)
            pasos.append({
                "tipo":      "solucion",
                "celda":     actual,
                "visitados": set(visitados),
                "camino":    camino,
                "frontera":  [],
                "mensaje":   (
                    f"¡META ENCONTRADA en {actual}!\n"
                    f"Camino: {' → '.join(str(c) for c in camino)}\n"
                    f"Longitud: {len(camino) - 1} pasos"
                )
            })
            return pasos, {
                "Solución":        "Sí",
                "Longitud camino": len(camino) - 1,
                "Nodos visitados": len(visitados),
            }

        vecinos = obtener_vecinos(actual)
        msg = f"Nodo actual: {actual}\nVecinos posibles: {vecinos}\n"

        for vecino in vecinos:
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = actual
                cola.append(vecino)
                msg += f"  → {vecino} no visitado, se agrega a la cola\n"
            else:
                msg += f"  → {vecino} ya visitado, se ignora\n"

        pasos.append({
            "tipo":      "expansion",
            "celda":     actual,
            "visitados": set(visitados),
            "frontera":  list(cola),
            "mensaje":   msg.strip()
        })

    pasos.append({
        "tipo":    "fracaso",
        "mensaje": "No hay camino a la meta"
    })
    return pasos, {"Solución": "No", "Nodos visitados": len(visitados)}

# DFS — Búsqueda en Profundidad

def dfs():
    pasos     = []
    pila      = []
    padres    = {}
    visitados = set()

    pila.append(INICIO)
    visitados.add(INICIO)
    padres[INICIO] = None

    pasos.append({
        "tipo":      "inicio",
        "celda":     INICIO,
        "visitados": set(visitados),
        "frontera":  list(pila),
        "mensaje":   (
            f"DFS inicia en {INICIO}\n"
            f"Se apila {INICIO}\n"
            f"Meta: {META}"
        )
    })

    while len(pila) > 0:
        actual = pila.pop()

        if actual == META:
            camino = reconstruir_camino(padres, actual)
            pasos.append({
                "tipo":      "solucion",
                "celda":     actual,
                "visitados": set(visitados),
                "camino":    camino,
                "frontera":  [],
                "mensaje":   (
                    f"¡META ENCONTRADA en {actual}!\n"
                    f"Camino: {' → '.join(str(c) for c in camino)}\n"
                    f"Longitud: {len(camino) - 1} pasos"
                )
            })
            return pasos, {
                "Solución":        "Sí",
                "Longitud camino": len(camino) - 1,
                "Nodos visitados": len(visitados),
            }

        vecinos = obtener_vecinos(actual)
        msg = f"Nodo actual: {actual}\nVecinos posibles: {vecinos}\n"
        for vecino in reversed(vecinos):
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = actual
                pila.append(vecino)
                msg += f"  → {vecino} no visitado, se apila\n"
            else:
                msg += f"  → {vecino} ya visitado, se ignora\n"

        pasos.append({
            "tipo":      "expansion",
            "celda":     actual,
            "visitados": set(visitados),
            "frontera":  list(pila),
            "mensaje":   msg.strip()
        })

    pasos.append({
        "tipo":    "fracaso",
        "mensaje": "No hay camino a la meta"
    })
    return pasos, {"Solución": "No", "Nodos visitados": len(visitados)}
