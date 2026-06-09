"""
Búsqueda Informada - Grid con paredes (4×7)
Algoritmos: A* y Greedy Best-First

Grid:
  Fila 0:  .  X  .  .  .  .  .
  Fila 1:  .  .  .  X  F  X  X   ← F = Meta (1,4)
  Fila 2:  .  X  .  X  .  .  .
  Fila 3:  I  X  .  .  .  .  .   ← I = Inicio (3,0)

Heurística  Manhattan
"""

import heapq

GRID = [
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
]
INICIO  = (3, 0)
META    = (1, 4)
FILAS   = 4
COLS    = 7

DIRECCIONES = [(-1,0), (1,0), (0,-1), (0,1)]


def celda_valida(fila, col):
    if fila < 0 or fila >= FILAS:
        return False
    if col < 0 or col >= COLS:
        return False
    if GRID[fila][col] == 1:
        return False
    return True


def obtener_vecinos(celda):
    fila, col = celda
    vecinos   = []
    for df, dc in DIRECCIONES:
        nf = fila + df
        nc = col  + dc
        if celda_valida(nf, nc):
            vecinos.append((nf, nc))
    return vecinos


def heuristica(celda):
    fm, cm = META
    fa, ca = celda
    return abs(fa - fm) + abs(ca - cm)


def h_todas_las_celdas():
    valores = {}
    for i in range(FILAS):
        for j in range(COLS):
            if GRID[i][j] == 0:
                valores[(i, j)] = heuristica((i, j))
    return valores


def reconstruir_camino(padres, nodo):
    camino = []
    actual = nodo
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    camino.reverse()
    return camino


def hacer_paso(celda, visitados, open_set, closed_list, camino, g, h, f, msg):
    return {
        "tipo":       "expansion",
        "celda":      celda,
        "visitados":  set(visitados),
        "open_set":   dict(open_set),
        "closed_set": list(closed_list),
        "camino":     list(camino),
        "h_grid":     h_todas_las_celdas(),
        "g": g, "h": h, "f": f,
        "mensaje":    msg,
    }

# A* — A Estrella

def a_star():
    pasos    = []
    padres   = {INICIO: None}
    visitados = {}
    contador = 0
    h0 = heuristica(INICIO)
    g0 = 0
    f0 = g0 + h0
    cola    = [(f0, contador, g0, INICIO)]
    open_   = {INICIO: f0}
    closed  = []

    pasos.append({
        "tipo":       "inicio",
        "celda":      INICIO,
        "visitados":  set(),
        "open_set":   {INICIO: f0},
        "closed_set": [],
        "camino":     [INICIO],
        "h_grid":     h_todas_las_celdas(),
        "g": g0, "h": h0, "f": f0,
        "mensaje": (
            f"A* inicia\n"
            f"Inicio: {INICIO} | Meta: {META}\n"
            f"h({INICIO}) = |3-1| + |0-4| = {h0}  ← distancia Manhattan\n"
            f"f = g + h = 0 + {h0} = {f0}\n"
            f"OPEN  = [{INICIO}  f={f0}]\n"
            f"CLOSED = []"
        )
    })

    nodos_expandidos = 0

    while len(cola) > 0:
        f_cur, _, g_cur, celda = heapq.heappop(cola)
        if celda in visitados and visitados[celda] <= g_cur:
            continue

        visitados[celda] = g_cur
        if celda in open_:
            del open_[celda]
        closed.append(celda)
        nodos_expandidos += 1
        if celda == META:
            camino = reconstruir_camino(padres, celda)
            pasos.append({
                "tipo":       "solucion",
                "celda":      celda,
                "visitados":  set(visitados.keys()),
                "open_set":   dict(open_),
                "closed_set": list(closed),
                "camino":     camino,
                "h_grid":     h_todas_las_celdas(),
                "g": g_cur, "h": 0, "f": g_cur,
                "mensaje": (
                    f"¡META ENCONTRADA!\n"
                    f"Camino óptimo: {' → '.join(str(c) for c in camino)}\n"
                    f"Costo total g = {g_cur} pasos\n"
                    f"Nodos expandidos (CLOSED): {len(closed)}"
                )
            })
            return pasos, {
                "Solución":         "Sí",
                "Costo g(n)":       g_cur,
                "Longitud camino":  len(camino) - 1,
                "Nodos expandidos": nodos_expandidos,
                "OPEN al final":    len(open_),
            }

        vecinos = obtener_vecinos(celda)
        lineas_vecinos = []

        for v in vecinos:
            nuevo_g = g_cur + 1
            nuevo_h = heuristica(v)
            nuevo_f = nuevo_g + nuevo_h

            if v not in visitados or visitados.get(v, 999) > nuevo_g:
                padres[v] = celda
                contador  += 1
                heapq.heappush(cola, (nuevo_f, contador, nuevo_g, v))
                open_[v] = nuevo_f
                lineas_vecinos.append(
                    f"    {v}: g={nuevo_g} + h={nuevo_h} = f={nuevo_f}"
                )

        camino_actual = reconstruir_camino(padres, celda)
        open_str  = "  ".join(f"{c}(f={v})" for c, v in sorted(open_.items(), key=lambda x: x[1]))
        h_celda   = heuristica(celda)

        msg = (
            f"Paso {nodos_expandidos}: Expandir {celda}\n"
            f"  g={g_cur} (pasos desde inicio)  h={h_celda} (heurística)  f={g_cur+h_celda}\n"
            f"  Vecinos evaluados:\n"
        )
        if lineas_vecinos:
            msg += "\n".join(lineas_vecinos) + "\n"
        else:
            msg += "    (sin vecinos nuevos)\n"
        msg += f"  CLOSED = {closed}\n"
        msg += f"  OPEN   = {open_str if open_str else '(vacío)'}"

        pasos.append(hacer_paso(
            celda, set(visitados.keys()), open_, closed,
            camino_actual, g_cur, h_celda, g_cur + h_celda, msg
        ))

    pasos.append({"tipo": "fracaso", "mensaje": "No hay camino a la meta"})
    return pasos, {"Solución": "No", "Nodos expandidos": nodos_expandidos}


# Greedy Best-First Search

def greedy_bfs():
    pasos    = []
    padres   = {INICIO: None}
    visitados = set()
    contador = 0

    h0 = heuristica(INICIO)

    cola   = [(h0, contador, INICIO)]
    open_  = {INICIO: h0}
    closed = []

    pasos.append({
        "tipo":       "inicio",
        "celda":      INICIO,
        "visitados":  set(),
        "open_set":   {INICIO: h0},
        "closed_set": [],
        "camino":     [INICIO],
        "h_grid":     h_todas_las_celdas(),
        "g": 0, "h": h0, "f": h0,
        "mensaje": (
            f"Greedy Best-First inicia\n"
            f"Inicio: {INICIO} | Meta: {META}\n"
            f"h({INICIO}) = {h0}  ← Greedy usa SOLO h(n)\n"
            f"No considera g(n): puede no ser óptimo\n"
            f"OPEN  = [{INICIO}  h={h0}]\n"
            f"CLOSED = []"
        )
    })

    nodos_expandidos = 0

    while len(cola) > 0:
        h_cur, _, celda = heapq.heappop(cola)

        if celda in visitados:
            continue
        visitados.add(celda)
        if celda in open_:
            del open_[celda]
        closed.append(celda)
        nodos_expandidos += 1

        if celda == META:
            camino = reconstruir_camino(padres, celda)
            pasos.append({
                "tipo":       "solucion",
                "celda":      celda,
                "visitados":  set(visitados),
                "open_set":   dict(open_),
                "closed_set": list(closed),
                "camino":     camino,
                "h_grid":     h_todas_las_celdas(),
                "g": len(camino)-1, "h": 0, "f": 0,
                "mensaje": (
                    f"¡META ENCONTRADA!\n"
                    f"Camino: {' → '.join(str(c) for c in camino)}\n"
                    f"Longitud: {len(camino)-1} pasos\n"
                    f"Nota: puede no ser el camino más corto\n"
                    f"Nodos expandidos: {len(closed)}"
                )
            })
            return pasos, {
                "Solución":         "Sí",
                "Longitud camino":  len(camino) - 1,
                "Nodos expandidos": nodos_expandidos,
            }

        vecinos = obtener_vecinos(celda)
        lineas_vecinos = []

        for v in vecinos:
            if v not in visitados:
                nuevo_h = heuristica(v)
                padres[v] = celda
                contador += 1
                heapq.heappush(cola, (nuevo_h, contador, v))
                open_[v] = nuevo_h
                lineas_vecinos.append(f"    {v}: h={nuevo_h}")

        camino_actual = reconstruir_camino(padres, celda)
        open_str = "  ".join(f"{c}(h={v})" for c, v in sorted(open_.items(), key=lambda x: x[1]))

        msg = (
            f"Paso {nodos_expandidos}: Expandir {celda}\n"
            f"  h={h_cur} (solo heurística, ignoramos g)\n"
            f"  Vecinos evaluados:\n"
        )
        if lineas_vecinos:
            msg += "\n".join(lineas_vecinos) + "\n"
        else:
            msg += "    (sin vecinos nuevos)\n"
        msg += f"  CLOSED = {closed}\n"
        msg += f"  OPEN   = {open_str if open_str else '(vacío)'}"

        pasos.append(hacer_paso(
            celda, set(visitados), open_, closed,
            camino_actual, len(camino_actual)-1, h_cur, h_cur, msg
        ))

    pasos.append({"tipo": "fracaso", "mensaje": "No hay camino a la meta"})
    return pasos, {"Solución": "No", "Nodos expandidos": nodos_expandidos}
