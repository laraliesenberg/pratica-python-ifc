def fatorial(n): 
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
n = 4
print(f'O fatorial de {n} é {fatorial(n)}')
