def tokenização(expressao):
    lista_operadores = ["+", "-", "*", "/", "^", "(", ")"]
    lista = []
    numero = ""
    expressao = expressao.strip()

    for i in range(len(expressao)):
        if expressao[i].isdigit():
            numero = numero + expressao[i]
        else: 
            if numero:
                lista.append(numero)
                numero = ""
            if expressao[i] in lista_operadores:
                lista.append(expressao[i])
    if numero: 
        lista.append(numero)
    return lista
                
def main():
    expressao = str(input("Digite uma expressão: "))
    tokens = tokenização(expressao)
    print("Tokens:", tokens)

if __name__ == "__main__":
    main()