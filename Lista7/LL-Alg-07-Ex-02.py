def diferença_simétrica(M, N):
    diferenca = M ^ N
    lista = sorted(diferenca)
    return lista

def main():
    M = {2, 4, 5, 9}
    N = {2, 11, 12}
    resultado = diferença_simétrica(M, N)
    print(resultado)

if __name__ == "__main__":
    main()