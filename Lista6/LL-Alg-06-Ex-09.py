lista= []
lista_menor = []
lista_media = []
lista_maior = []
soma = 0

while True:
    result = input("Digite um número inteiro: ")
    if result == "":
        break
    else:
        n = int(result)
        lista.append(n)
        soma += n
media = soma / len(lista)

for i in range(len(lista)):
    if lista[i] < media:
        lista_menor.append(lista[i])
    elif lista[i] == media:
        lista_media.append(lista[i])
    else:
        lista_maior.append(lista[i])

print("A média é:", media)
print("Valores abaixo da média:", lista_menor)
print("Valores médios:", lista_media)
print("Valores acima da média:", lista_maior)