def a_lista_esta_ordenada(lista):
    lista_ordenada_crescente = sorted(lista)
    lista_ordenada_decrescente = sorted(lista, reverse=True)
    if lista == lista_ordenada_crescente or lista == lista_ordenada_decrescente:
        return True
    else:
        return False

def main():
    lista = []
    while True:
        n = input("Digite um valor(enter para parar):")
        if n == "":
            break
        else:
            result = int(n)
            lista.append(result)      
    if a_lista_esta_ordenada(lista):
        print("Classificado")
    else:
        print("Não classificado")

if __name__ == "__main__":
    main()