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

def main():
    infix = ["3", "+", "4", "*", "(", "2", "+", "5", ")"]
    postfix = infix_para_postfix(infix)
    print(" ".join(postfix))

if __name__ == "__main__":
    main()