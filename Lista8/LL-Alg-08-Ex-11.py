def codificação_run_lenght(lista_codificada):
    if not lista_codificada:
        return []
    i = 1
    while i < len(lista_codificada) and lista_codificada[0] == lista_codificada[i]:
        i = i + 1
    return [lista_codificada[0], i] + codificação_run_lenght(lista_codificada[i:])

def main():
    lista_decodificada = ["A", "A", "A", "A", "B", "B", "A", "C", "C", "C", "C", "C"]
    lista_codificada = codificação_run_lenght(lista_decodificada)
    print(f'Lista decodificada: {lista_decodificada}')
    print(f'Lista codificada: {lista_codificada}')

if __name__ == "__main__":
    main()