def decodificação_run_lenght(lista_codificada):
    if not lista_codificada:
        return []
    valores = lista_codificada[0]
    repeticoes = lista_codificada[1]
    total = [valores] * repeticoes

    lista_restante = decodificação_run_lenght(lista_codificada[2:])

    return total + lista_restante

def main():
    lista_codificada = ["A", 12, "B", 4, "A", 6, "B", 1]
    lista_decodificada = decodificação_run_lenght(lista_codificada)
    print(f'Lista codificada: {lista_codificada}')
    print(f'Lista decodificada: {lista_decodificada}')

if __name__ == "__main__":
    main()