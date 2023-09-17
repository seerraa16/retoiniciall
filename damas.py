def zona_segura(tablero, fila, columna, n):
    return all(
        tablero[i][columna] == 0 and
        tablero[i][j] == 0
        for i, j in zip(range(fila, -1, -1), range(columna, -1, -1))) and \
        all(
            tablero[i][j] == 0
            for i, j in zip(range(fila, -1, -1), range(columna, n))) and \
        all(
            tablero[i][columna] == 0
            for i in range(fila)
    )

def numero_soluciones(n):
    def backtrack(fila):
        nonlocal soluciones
        if fila == n:
            soluciones += 1
            return
        for columna in range(n):
            if zona_segura(tablero, fila, columna, n):
                tablero[fila][columna] = 1
                backtrack(fila + 1)
                tablero[fila][columna] = 0
    
    tablero = [[0] * n for _ in range(n)]
    soluciones = 0
    backtrack(0)
    return soluciones

# Número de damas
N = 15

soluciones = numero_soluciones(N)
print(f'Para n={N}, hay {soluciones} soluciones.')
