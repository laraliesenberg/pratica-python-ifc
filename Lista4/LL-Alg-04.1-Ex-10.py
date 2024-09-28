n = int(input("Digite um número inteiro positivo:"))

A = 0
denominador = 1
while denominador <= n:
    print("1 /", denominador)
    A = A + 1/denominador
    denominador = denominador + 2
print(A)
