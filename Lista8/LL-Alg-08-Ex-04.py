dicionário = {0: 0, 1: 1}
def fibonacci_com_memorização(n):
    if n in dicionário:
        return dicionário[n]
    resultado = fibonacci_com_memorização(n - 1) + fibonacci_com_memorização(n - 2)
    dicionário[n] = resultado
    return resultado

n = 30
print(f'O {n}º termo da série de Fibonacci é {fibonacci_com_memorização(n)}')