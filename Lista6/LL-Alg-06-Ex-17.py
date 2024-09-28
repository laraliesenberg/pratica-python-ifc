def precedencia(operador):
    if operador == "+" or operador == "-":
        return 1
    if operador == "*" or operador == "/":
        return 2
    if operador == "^":
        return 3
    else:
        return -1
    
def infix_para_postfix(infix):
    operadores = []
    postfix = []

    for token in infix:
        if token.isdigit():
            postfix.append(token)
        elif token in '+-*/^':
            while (operadores and operadores[-1] != '(' and precedencia(token) < precedencia(operadores[-1])):
                postfix.append(operadores[-1])
                operadores = operadores[:-1] 
            operadores.append(token)
        elif token == '(':
            operadores.append(token)
        elif token == ')':
            while operadores[-1] != '(':
                postfix.append(operadores[-1])
                operadores = operadores[:-1] 
            operadores = operadores[:-1]
    while operadores:
        postfix.append(operadores[-1])
        operadores = operadores[:-1] 
        
    return postfix


def avaliação_de_expresssão(expressao_postfix):
    valores = []
    for token in expressao_postfix:
        if token.isdigit():
            valores.append(int(token))
        else:
            direita = valores.pop()
            esquerda = valores.pop()
            if token == "+":
                resultado = esquerda + direita
            elif token == "-":
                resultado = esquerda - direita
            elif token == "*":
                resultado = esquerda * direita
            elif token == "/":
                resultado = esquerda / direita
            elif token == "^":
                resultado = esquerda ** direita
            valores.append(resultado)

    return valores[0]

def main():
    infix = input("Digite uma expressão em formato infixo: ")

    expressao_postfix = infix_para_postfix(infix)
    print(f"Expressão pós-fixada: {' '.join(expressao_postfix)}")

    resultado = avaliação_de_expresssão(expressao_postfix)
    print(f'Resultado: {resultado}')

if __name__ == "__main__":
    main()