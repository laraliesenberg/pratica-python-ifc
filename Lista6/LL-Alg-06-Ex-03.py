def removendo_extremos(lista, n):
    lista_nova = []
    lista.sort()
    lista_nova = lista[n:-n]
    return lista_nova


def main():
    lista = []
    n = 2 
    while True:
        x = int(input("Digite um número inteiro(0 para parar):"))
        if x == 0:
            break
        lista.append(x)
    if len(lista) < 4:
        print("Não pode lista com menos de 4 dígitos")
    else:
        print("lista nova:", removendo_extremos(lista, n))
        print("lista antiga", lista)

if __name__ == "__main__":
    main() 