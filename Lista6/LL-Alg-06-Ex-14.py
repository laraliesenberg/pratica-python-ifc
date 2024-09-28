def precedencia(operador):
    if operador == "+" or operador == "-":
        return 1
    if operador == "*" or operador == "/":
        return 2
    if operador == "^":
        return 3
    else:
        return -1

def main():
    operador = input("Digite um operador matemático: ")
    operador_matematico = precedencia(operador)
    if operador_matematico == -1:
        print("Erro! Não é um operador")
    else:
        print("{:d}".format(operador_matematico))
             
if __name__ == "__main__":
    main()