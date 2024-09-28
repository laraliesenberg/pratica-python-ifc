def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = 30
print(f'O {n}º termo da série de Fibonacci é {fibonacci(n)}')