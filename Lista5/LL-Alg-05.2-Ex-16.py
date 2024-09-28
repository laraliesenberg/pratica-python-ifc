def convertendo_para_decimal(n, base):
    return int(n, base)

def converter_o_decimal(decimal, base):
    digitos = "0123456789ABCDEF"
    if decimal == 0:
        return "0"
    resultado = ""
    while decimal > 0:
        resto = decimal % base
        resultado = digitos[resto] + resultado
        decimal //= base
    return resultado

def main():
    base_entrada = int(input("Digite a base do número(2-16): "))
    if base_entrada < 2 or base_entrada > 16:
        print("Base inválida.")
        return
    n = input("Digite o número que deseja converter: ").upper()

    decimal = convertendo_para_decimal(n, base_entrada)

    base_saida = int(input("Digite a base para converter(2-16): "))
    if base_saida < 2 or base_saida > 16:
        print("Base inválida.")
        return

    resultado = converter_o_decimal(decimal, base_saida)
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()