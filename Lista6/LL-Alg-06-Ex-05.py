lista_negativos= []
lista_zero = []
lista_positivos = []

while True:
    result = input("Digite um número inteiro(positivos ou negativos): ")
    if result == "":
        break
    n = int(result)
    if n < 0:
        lista_negativos.append(n)
    elif n == 0:
        lista_zero.append(n)
    elif n > 0:
        lista_positivos.append(n)

lista = lista_negativos + lista_zero + lista_positivos
for i in range(len(lista)):
    print(lista[i])