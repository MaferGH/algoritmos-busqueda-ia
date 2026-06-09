"""
Búsqueda Local - Problema de las N-Reinas (8 reinas)
Algoritmos: Hill Climbing y Simulated Annealing

  Dos reinas SE ATACAN si:
    1. Están en la MISMA COLUMNA: estado[i] == estado[j]
    2. Están en la MISMA DIAGONAL: |estado[i]-estado[j]| == |i-j|
"""

import random
import math


def calcular_conflictos(estado):
    n          = len(estado)
    conflictos = 0
    for i in range(n):
        for j in range(i + 1, n):
            misma_columna  = (estado[i] == estado[j])
            misma_diagonal = (abs(estado[i] - estado[j]) == abs(i - j))
            if misma_columna or misma_diagonal:
                conflictos += 1
    return conflictos


def celdas_en_conflicto(estado):
    n          = len(estado)
    en_conflicto = set()
    for i in range(n):
        for j in range(i + 1, n):
            if estado[i] == estado[j] or abs(estado[i]-estado[j]) == abs(i-j):
                en_conflicto.add(i)
                en_conflicto.add(j)
    return en_conflicto


def estado_aleatorio(n=8):
    return [random.randint(0, n-1) for _ in range(n)]


def mejor_vecino(estado):
    n             = len(estado)
    mejor_estado  = None
    mejor_conf    = calcular_conflictos(estado)
    mejor_fila    = -1
    mejor_col_ant = -1
    mejor_col_nva = -1

    for fila in range(n):
        col_actual = estado[fila]
        for nueva_col in range(n):
            if nueva_col == col_actual:
                continue
            vecino       = estado[:]
            vecino[fila] = nueva_col
            conf         = calcular_conflictos(vecino)

            if conf < mejor_conf:
                mejor_conf    = conf
                mejor_estado  = vecino
                mejor_fila    = fila
                mejor_col_ant = col_actual
                mejor_col_nva = nueva_col

    return mejor_estado, mejor_fila, mejor_col_ant, mejor_col_nva, mejor_conf


def hacer_paso_reinas(estado, conflictos, iteracion, fila_mov, col_ant, col_nva, msg):
    return {
        "tipo":        "movimiento",
        "estado":      estado[:],
        "conflictos":  conflictos,
        "iteracion":   iteracion,
        "reina_movida":fila_mov,
        "col_anterior":col_ant,
        "col_nueva":   col_nva,
        "en_conflicto":celdas_en_conflicto(estado),
        "mensaje":     msg,
    }

# Hill Climbing

def hill_climbing(estado_inicial=None):
    pasos = []

    if estado_inicial is None:
        estado_inicial = estado_aleatorio()

    estado     = estado_inicial[:]
    conflictos = calcular_conflictos(estado)
    iteracion  = 0

    pasos.append({
        "tipo":         "inicio",
        "estado":       estado[:],
        "conflictos":   conflictos,
        "iteracion":    0,
        "reina_movida": -1,
        "col_anterior": -1,
        "col_nueva":    -1,
        "en_conflicto": celdas_en_conflicto(estado),
        "mensaje": (
            f"Hill Climbing inicia\n"
            f"Estado inicial: {estado}\n"
            f"Conflictos iniciales: {conflictos}\n"
            f"Reinas en rojo = conflicto, en verde = seguras\n"
            f"Meta: llegar a 0 conflictos"
        )
    })

    while conflictos > 0:
        iteracion += 1
        nuevo, fila, col_ant, col_nva, nueva_conf = mejor_vecino(estado)

        if nuevo is None:
            pasos.append({
                "tipo":         "fin",
                "estado":       estado[:],
                "conflictos":   conflictos,
                "iteracion":    iteracion,
                "reina_movida": -1,
                "col_anterior": -1,
                "col_nueva":    -1,
                "en_conflicto": celdas_en_conflicto(estado),
                "mensaje": (
                    f"Paso {iteracion}: ÓPTIMO LOCAL\n"
                    f"Ningún movimiento reduce los conflictos.\n"
                    f"Hill Climbing se detiene con {conflictos} conflictos.\n"
                    f"(Para escapar: usar Random Restart o SA)"
                )
            })
            break

        msg = (
            f"Paso {iteracion}: Mover reina en fila {fila}\n"
            f"  Columna {col_ant} → columna {col_nva}\n"
            f"  Conflictos: {conflictos} → {nueva_conf}\n"
            f"  Mejora: {conflictos - nueva_conf} conflictos menos\n"
            f"  (Se evaluaron todos los movimientos posibles)"
        )

        estado     = nuevo
        conflictos = nueva_conf
        pasos.append(hacer_paso_reinas(estado, conflictos, iteracion,
                                        fila, col_ant, col_nva, msg))

    if conflictos == 0:
        pasos.append({
            "tipo":         "fin_ok",
            "estado":       estado[:],
            "conflictos":   0,
            "iteracion":    iteracion,
            "reina_movida": -1,
            "col_anterior": -1,
            "col_nueva":    -1,
            "en_conflicto": set(),
            "mensaje": (
                f"¡SOLUCIÓN ENCONTRADA!\n"
                f"Estado: {estado}\n"
                f"0 conflictos en {iteracion} pasos"
            )
        })

    return pasos, {
        "Solución":           "Sí" if conflictos == 0 else "No (óptimo local)",
        "Conflictos finales": conflictos,
        "Iteraciones":        iteracion,
    }

# Recocido Simulado

def simulated_annealing(estado_inicial=None):
    pasos = []

    if estado_inicial is None:
        estado_inicial = estado_aleatorio()

    estado      = estado_inicial[:]
    conflictos  = calcular_conflictos(estado)
    temperatura = 10.0
    enfriamiento= 0.98
    temp_minima = 0.01
    iteracion   = 0

    pasos.append({
        "tipo":         "inicio",
        "estado":       estado[:],
        "conflictos":   conflictos,
        "iteracion":    0,
        "temperatura":  round(temperatura, 3),
        "reina_movida": -1,
        "col_anterior": -1,
        "col_nueva":    -1,
        "en_conflicto": celdas_en_conflicto(estado),
        "mensaje": (
            f"Simulated Annealing inicia\n"
            f"Estado inicial: {estado}\n"
            f"Conflictos: {conflictos}\n"
            f"Temperatura T={temperatura} (alta = acepta casi todo)\n"
            f"Enfriamiento: T = T × {enfriamiento} en cada paso"
        )
    })

    while temperatura > temp_minima and conflictos > 0:
        iteracion += 1
        n         = len(estado)
        fila      = random.randint(0, n - 1)
        nueva_col = random.randint(0, n - 1)
        while nueva_col == estado[fila]:
            nueva_col = random.randint(0, n - 1)

        vecino     = estado[:]
        vecino[fila] = nueva_col
        nueva_conf = calcular_conflictos(vecino)
        delta      = nueva_conf - conflictos
        if delta < 0:
            aceptado = True
            razon    = f"MEJOR (delta={delta}, siempre se acepta)"
        else:
            prob     = math.exp(-delta / temperatura)
            aceptado = (random.random() < prob)
            razon    = (
                f"PEOR (delta=+{delta}), "
                f"probabilidad={prob:.3f} → "
                f"{'ACEPTADO (escapa)' if aceptado else 'RECHAZADO'}"
            )

        if aceptado:
            col_ant    = estado[fila]
            estado     = vecino
            conflictos = nueva_conf
        else:
            col_ant    = estado[fila]
            nueva_col  = col_ant

        temperatura = temperatura * enfriamiento
        
        if iteracion % 20 == 0 or conflictos == 0 or aceptado:
            msg = (
                f"Iter {iteracion}: Reina fila {fila}, col {col_ant} → col {nueva_col}\n"
                f"  {razon}\n"
                f"  Conflictos: {conflictos}\n"
                f"  Temperatura actual: T={temperatura:.4f}"
            )
            pasos.append({
                "tipo":         "movimiento",
                "estado":       estado[:],
                "conflictos":   conflictos,
                "iteracion":    iteracion,
                "temperatura":  round(temperatura, 4),
                "reina_movida": fila if aceptado else -1,
                "col_anterior": col_ant,
                "col_nueva":    nueva_col if aceptado else col_ant,
                "en_conflicto": celdas_en_conflicto(estado),
                "mensaje":      msg,
            })

    tipo_fin = "fin_ok" if conflictos == 0 else "fin"
    pasos.append({
        "tipo":         tipo_fin,
        "estado":       estado[:],
        "conflictos":   conflictos,
        "iteracion":    iteracion,
        "temperatura":  round(temperatura, 4),
        "reina_movida": -1,
        "col_anterior": -1,
        "col_nueva":    -1,
        "en_conflicto": celdas_en_conflicto(estado),
        "mensaje": (
            f"{'¡SOLUCIÓN!' if conflictos==0 else 'Temperatura agotada'}\n"
            f"Estado final: {estado}\n"
            f"Conflictos: {conflictos}\n"
            f"Iteraciones: {iteracion}\n"
            f"Temperatura final: {round(temperatura,4)}"
        )
    })

    return pasos, {
        "Solución":           "Sí" if conflictos == 0 else "No",
        "Conflictos finales": conflictos,
        "Temperatura final":  round(temperatura, 4),
        "Iteraciones":        iteracion,
    }
