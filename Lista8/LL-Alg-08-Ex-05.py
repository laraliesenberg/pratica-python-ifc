def total_valores_numericos():
    valor = input("Digite um valor(enter para parar): ") 
    if valor == "":
        return 0.0
    elif not valor.replace('.', '', 1).isdigit():
        print("Esse valor não é válido")
        return total_valores_numericos()
    else:
        valor_float = float(valor)
        return valor_float + total_valores_numericos()


def main():
    total = total_valores_numericos()
    print(f'A soma total dos valores é {total}')

if __name__ == "__main__":
    main()