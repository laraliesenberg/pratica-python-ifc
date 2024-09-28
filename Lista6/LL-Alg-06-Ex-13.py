def countRange(lista, maximo, minimo):
    quantidade = 0
    for i in range(len(lista)):
        if lista[i] >= minimo and lista[i] < maximo:
            quantidade = quantidade + 1
    return quantidade

def main():
    lista = [2, 4, 8, 16, 32, 64, 128, 256]
    maximo = 128
    minimo = 4
    total = countRange(lista, maximo, minimo)
    print(total)

if __name__ == "__main__":
    main()