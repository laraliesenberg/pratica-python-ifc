def formatando_lista(lista):
    tamanho = len(lista)
    if tamanho == 0:
        return ""
    elif tamanho == 1:
        return lista[0]
    elif tamanho == 2:
        return f"{lista[0]} e {lista[1]}"
    else:
        return ", ".join(lista[:-1]) + " e " + lista[-1]

def main():
    lista = []
    while True:
        palavra = str(input("Digite uma palavra: "))
        if palavra == "":
            break
        else:
            lista.append(palavra)
    print(formatando_lista(lista))

if __name__ == "__main__":
    main()