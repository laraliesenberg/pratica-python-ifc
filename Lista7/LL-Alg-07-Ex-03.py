def buscaReversa(dicionario, valores):
    lista = []
    for chave, valor in dicionario.items():
        if valores == valor:
            lista.append(chave)
    return lista

def main():
    dicionario = {1: 'laranja', 2: 'maçã', 3: 'pera', 4: 'maçã'}
    valores = 'maçã'
    lista_oficial = buscaReversa(dicionario, valores)
    print(lista_oficial)

if __name__ == "__main__":
    main()