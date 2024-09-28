def potencia(x, y):
    resultado = 1
    i = 0
    while i < y:
        resultado = resultado * x
        i = i + 1
    print(f'O valor de {x} elevado a {y} é {resultado}')
potencia(2, 4)