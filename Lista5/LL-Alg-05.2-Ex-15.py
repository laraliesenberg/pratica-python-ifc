def hex2int(n1):
    n1 = n1.upper()
    lista1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if n1 in lista1:
        return lista1.index(n1)
    else:
        return False

def int2hex(n2):
    lista2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if n2 >= 0 and n2 <= 15:
        return lista2[n2]
    else:
        return False

def main():
    n1 = input("Digite um dígito hexadecimal: ")
    if len(n1) == 1:
        resultado_decimal = hex2int(n1)
        print("Valor decimal:", resultado_decimal)
    else:
        print("Apenas um dígito")

    n2 = int(input("Digite um número decimal (entre 0 e 15): "))
    if len(n1) == 1:
        resultado_hexadecimal = int2hex(n2)
        print("Valor hexadecimal:", resultado_hexadecimal)
    else:
        print("Apenas um dígito")

if __name__ == "__main__":
    main()
