def raiz_quadrada(n, estimativa = 1.0):
    diferenca = abs((estimativa * estimativa) - n)
    
    if diferenca <= 10 ** -12:
        return estimativa
    else:
        estimativa_oficial = (estimativa + n / estimativa) / 2
        return raiz_quadrada(n, estimativa_oficial)

def main():
    valores = [4, 9, 25, 2, 144, 169]
    for valor in valores:
        resultado = raiz_quadrada(valor)
        print(f"A raiz quadrada de {valor} é aproximadamente {resultado:.12f}")

if __name__ == "__main__":
    main()