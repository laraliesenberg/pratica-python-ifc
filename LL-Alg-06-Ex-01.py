lista = []
while True:
    n = int(input("Digite um número inteiro(0 para parar): "))
    if n == 0:
        break
    lista.append(n)
lista.sort()
print(lista)