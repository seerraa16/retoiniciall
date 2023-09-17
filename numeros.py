#definimos cuantos movimientos puede hacer el caballo
def movimientos_caballo(x, y):
    movimientos = [(-2, -1), (-1, -2), (-2, 1), (-1, 2),
                   (1, -2), (2, -1), (1, 2), (2, 1)]
    contador = 0

    for dx, dy in movimientos:
        nuevo_x = x + dx
        nuevo_y = y + dy
        if 1 <= nuevo_x <= 3 and 1 <= nuevo_y <= 3:
            contador += 1

    return contador




