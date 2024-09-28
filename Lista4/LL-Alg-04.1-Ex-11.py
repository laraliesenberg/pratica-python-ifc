n = int(input("Digite um número inteiro positivo:"))

A = 0 
denominador = 1

while denominador <= n:
    if denominador % 2 == 0:
        A = A - 1 / denominador 
    else:
        A = A + 1 / denominador 
    denominador = denominador + 1 
print(A)


