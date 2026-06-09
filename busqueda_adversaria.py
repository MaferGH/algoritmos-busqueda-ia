"""
Búsqueda Adversaria - Tic-Tac-Toe (Gato)
Algoritmos: Minimax y Minimax con poda Alpha-Beta

X = jugador MAX (quiere puntaje alto)
O = jugador MIN (quiere puntaje bajo)
"""

VACIO = " "
X = "X"
O = "O"

LINEAS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]


def mostrar_tablero(board):
    sep = "\n---+---+---\n"
    filas = []
    for i in range(3):
        c1 = board[i*3]; c2 = board[i*3+1]; c3 = board[i*3+2]
        filas.append(f" {c1} | {c2} | {c3} ")
    return sep.join(filas)


def verificar_ganador(board):
    for linea in LINEAS:
        a, b, c = linea
        if board[a] == board[b] == board[c] and board[a] != VACIO:
            return board[a]
    return None


def linea_ganadora(board):
    for linea in LINEAS:
        a, b, c = linea
        if board[a] == board[b] == board[c] and board[a] != VACIO:
            return linea
    return None


def tablero_lleno(board):
    for c in board:
        if c == VACIO:
            return False
    return True


def juego_terminado(board):
    if verificar_ganador(board) is not None:
        return True
    if tablero_lleno(board):
        return True
    return False


def celdas_libres(board):
    return [i for i in range(9) if board[i] == VACIO]


def hacer_jugada(board, pos, jugador):
    nuevo = board[:]
    nuevo[pos] = jugador
    return nuevo

# MINIMAX

def minimax_rec(board, es_max, profundidad):
    if juego_terminado(board):
        ganador = verificar_ganador(board)
        if ganador == X:
            return 10 - profundidad
        if ganador == O:
            return profundidad - 10
        return 0

    libres = celdas_libres(board)

    if es_max:
        mejor = -100
        for pos in libres:
            nuevo   = hacer_jugada(board, pos, X)
            puntaje = minimax_rec(nuevo, False, profundidad + 1)
            if puntaje > mejor:
                mejor = puntaje
        return mejor
    else:
        mejor = 100
        for pos in libres:
            nuevo   = hacer_jugada(board, pos, O)
            puntaje = minimax_rec(nuevo, True, profundidad + 1)
            if puntaje < mejor:
                mejor = puntaje
        return mejor


def minimax_wrapper(tablero_ini=None):
    if tablero_ini is None:
        tablero_ini = ["X", "O", VACIO,
                       VACIO, "X", VACIO,
                       "O", VACIO, VACIO]

    pasos  = []
    libres = celdas_libres(tablero_ini)

    pasos.append({
        "tipo":    "inicio",
        "tablero": tablero_ini[:],
        "mensaje": (
            f"Minimax inicia (turno de X)\n"
            f"Tablero:\n{mostrar_tablero(tablero_ini)}\n"
            f"X=MAX quiere el mayor puntaje\n"
            f"O=MIN quiere el menor puntaje\n"
            f"Casillas libres para X: {libres}"
        )
    })

    evaluaciones = []

    for pos in libres:
        nuevo   = hacer_jugada(tablero_ini, pos, X)
        puntaje = minimax_rec(nuevo, False, 1)
        evaluaciones.append((pos, puntaje))

        if puntaje > 0:
            etiqueta = f"X puede ganar (puntaje={puntaje})"
        elif puntaje < 0:
            etiqueta = f"X perdería (puntaje={puntaje})"
        else:
            etiqueta = "Empate"

        pasos.append({
            "tipo":         "evaluacion",
            "tablero":      nuevo[:],
            "pos_evaluada": pos,
            "valor":        puntaje,
            "mensaje": (
                f"X juega en posición {pos}:\n"
                f"{mostrar_tablero(nuevo)}\n"
                f"Minimax explora toda la rama...\n"
                f"Resultado: {etiqueta}"
            )
        })

    mejor_pos    = evaluaciones[0][0]
    mejor_punt   = evaluaciones[0][1]
    for pos, punt in evaluaciones:
        if punt > mejor_punt:
            mejor_punt = punt
            mejor_pos  = pos

    tablero_fin = hacer_jugada(tablero_ini, mejor_pos, X)
    linea       = linea_ganadora(tablero_fin)

    if mejor_punt > 0:
        resultado = "X gana"
    elif mejor_punt < 0:
        resultado = "O gana"
    else:
        resultado = "Empate"

    pasos.append({
        "tipo":                  "decision",
        "tablero":               tablero_fin[:],
        "mejor_movimiento":      mejor_pos,
        "valor":                 mejor_punt,
        "linea_ganadora":        linea,
        "movimientos_evaluados": evaluaciones,
        "mensaje": (
            f"Minimax elige posición {mejor_pos}\n"
            f"{mostrar_tablero(tablero_fin)}\n"
            f"Puntaje: {mejor_punt} → {resultado}\n"
            f"Evaluaciones: {evaluaciones}"
        )
    })

    return pasos, {
        "Mejor posición":     mejor_pos,
        "Puntaje":            mejor_punt,
        "Resultado esperado": resultado,
    }

# ALPHA-BETA PRUNING

def alphabeta_rec(board, es_max, profundidad, alpha, beta):
    if juego_terminado(board):
        ganador = verificar_ganador(board)
        if ganador == X:
            return 10 - profundidad
        if ganador == O:
            return profundidad - 10
        return 0

    libres = celdas_libres(board)

    if es_max:
        mejor = -100
        for pos in libres:
            nuevo   = hacer_jugada(board, pos, X)
            puntaje = alphabeta_rec(nuevo, False, profundidad+1, alpha, beta)
            if puntaje > mejor:
                mejor = puntaje
            if mejor > alpha:
                alpha = mejor
            if beta <= alpha:
                break
        return mejor
    else:
        mejor = 100
        for pos in libres:
            nuevo   = hacer_jugada(board, pos, O)
            puntaje = alphabeta_rec(nuevo, True, profundidad+1, alpha, beta)
            if puntaje < mejor:
                mejor = puntaje
            if mejor < beta:
                beta = mejor
            if beta <= alpha:
                break
        return mejor


def alphabeta_wrapper(tablero_ini=None):
    if tablero_ini is None:
        tablero_ini = ["X", "O", VACIO,
                       VACIO, "X", VACIO,
                       "O", VACIO, VACIO]

    pasos  = []
    libres = celdas_libres(tablero_ini)

    pasos.append({
        "tipo":    "inicio",
        "tablero": tablero_ini[:],
        "mensaje": (
            f"Alpha-Beta inicia (turno de X)\n"
            f"Tablero:\n{mostrar_tablero(tablero_ini)}\n"
            f"alpha = -inf (mejor para X=MAX)\n"
            f"beta  = +inf (mejor para O=MIN)\n"
            f"La poda descarta ramas que no cambiarán la decisión"
        )
    })

    evaluaciones = []
    alpha_global = -100

    for pos in libres:
        nuevo   = hacer_jugada(tablero_ini, pos, X)
        puntaje = alphabeta_rec(nuevo, False, 1, alpha_global, 100)
        evaluaciones.append((pos, puntaje))

        if puntaje > alpha_global:
            alpha_global = puntaje

        if puntaje > 0:
            etiqueta = f"X puede ganar (puntaje={puntaje})"
        elif puntaje < 0:
            etiqueta = f"X perdería (puntaje={puntaje})"
        else:
            etiqueta = "Empate"

        pasos.append({
            "tipo":         "evaluacion",
            "tablero":      nuevo[:],
            "pos_evaluada": pos,
            "valor":        puntaje,
            "mensaje": (
                f"X juega en posición {pos}:\n"
                f"{mostrar_tablero(nuevo)}\n"
                f"Alpha-Beta evalúa con α={alpha_global}, β=+inf\n"
                f"Resultado: {etiqueta}"
            )
        })

    mejor_pos  = evaluaciones[0][0]
    mejor_punt = evaluaciones[0][1]
    for pos, punt in evaluaciones:
        if punt > mejor_punt:
            mejor_punt = punt
            mejor_pos  = pos

    tablero_fin = hacer_jugada(tablero_ini, mejor_pos, X)
    linea       = linea_ganadora(tablero_fin)

    if mejor_punt > 0:
        resultado = "X gana"
    elif mejor_punt < 0:
        resultado = "O gana"
    else:
        resultado = "Empate"

    pasos.append({
        "tipo":                  "decision",
        "tablero":               tablero_fin[:],
        "mejor_movimiento":      mejor_pos,
        "valor":                 mejor_punt,
        "linea_ganadora":        linea,
        "movimientos_evaluados": evaluaciones,
        "mensaje": (
            f"Alpha-Beta elige posición {mejor_pos}\n"
            f"{mostrar_tablero(tablero_fin)}\n"
            f"Puntaje: {mejor_punt} → {resultado}\n"
            f"(Misma decisión que Minimax, menos nodos evaluados)"
        )
    })

    return pasos, {
        "Mejor posición":     mejor_pos,
        "Puntaje":            mejor_punt,
        "Resultado esperado": resultado,
    }


# MODO INTERACTIVO — la computadora (X) juega contra el usuario (O)

PREFERENCIA = [4, 0, 2, 6, 8, 1, 3, 5, 7]

def etiqueta_puntaje(punt):
    if punt >= 9:
        return "X GANA AHORA (3 en línea directa)"
    elif punt >= 7:
        return "X forzará 3 en línea en 3 turnos"
    elif punt >= 5:
        return "X forzará victoria más adelante"
    elif punt > 0:
        return "X tiene ventaja"
    elif punt == 0:
        return "Empate con juego perfecto"
    elif punt <= -9:
        return "O GANA AHORA (3 en línea directa)"
    elif punt <= -7:
        return "O forzará 3 en línea en 3 turnos"
    else:
        return "O tiene ventaja"


def computadora_juega(board, usar_alphabeta=False):
    libres = celdas_libres(board)
    if not libres:
        return None, 0, []

    mejor_pos  = None
    mejor_punt = -100
    evaluaciones = []
    for pos in PREFERENCIA:
        if pos not in libres:
            continue
        nuevo = hacer_jugada(board, pos, X)
        if usar_alphabeta:
            punt = alphabeta_rec(nuevo, False, 1, -100, 100)
        else:
            punt = minimax_rec(nuevo, False, 1)

        evaluaciones.append((pos, punt))

        if punt > mejor_punt:
            mejor_punt = punt
            mejor_pos  = pos

    return mejor_pos, mejor_punt, evaluaciones
