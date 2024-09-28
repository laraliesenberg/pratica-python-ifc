def MDC(a, b):
    if b == 0:
        return a
    else: 
        c = a % b
        return MDC(b, c)
    
a = 3
b = 9
print(f'O Máximo divisor comum é: {MDC(a, b)}')